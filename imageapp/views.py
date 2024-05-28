from django.urls import path
# imageapp/views.py

from django.shortcuts import render
import os

def image_list(request):
    image_dir = r'F:\GoogleDrive\python\web_draw_roi\roi_project\static\images'
    mask_dir = r'F:\GoogleDrive\python\web_draw_roi\roi_project\static\masks'
    images = os.listdir(image_dir)
    masks = [os.path.join(mask_dir, image) for image in images]
    return render(request, 'image_list.html', {'images': images, 'masks': masks})

def image_detail(request, image_name):
    image_dir = r'F:\GoogleDrive\python\web_draw_roi\roi_project\static\images'
    mask_dir = r'F:\GoogleDrive\python\web_draw_roi\roi_project\static\masks'
    image_path = os.path.join(image_dir, image_name)
    mask_path = os.path.join(mask_dir, image_name)
    return render(request, 'image_detail.html', {'image_path': image_path, 'mask_path': mask_path, 'image_name': image_name})