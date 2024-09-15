from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Car, Comment
from .forms import CarForm, CommentForm
from .serializers import CarSerializer, CommentSerializer

class CarListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            serializer = CarSerializer(car)
            return Response(serializer.data)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            if car.owner != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = CarSerializer(car, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            if car.owner != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CommentListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            comments = car.comment_set.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(car=car, author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars':cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    comments = car. comment_set.all()
    return render(request, 'cars/car_detail.html', {'car':car, 'comments':comments})

@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/add_car.html', {'form':form})

@login_required
def edit_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if car.owner != request.user:
        return redirect('car_list')
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_detail', pk=pk)
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/edit_car.html', {'form': form, 'car': car})

@login_required
def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if car.owner != request.user:
        return redirect('car_list')
    car.delete()
    return redirect('car_list')

@login_required
def add_comment(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.author = request.user
            comment.save()
            return redirect('car_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'cars/add_comment.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')