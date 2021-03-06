# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from api.models import *
from api.serializers import *
import pdb

class CompanyViewSet(viewsets.ModelViewSet):
    """
    RESTful API endpoint for Company
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def create(self, request):
        serializer = CompanyAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        request.data['password'] = '*' * len(request.data['password'])
        return JsonResponse({'request': request.data, 'status': 'created successfully'}, status=201)
