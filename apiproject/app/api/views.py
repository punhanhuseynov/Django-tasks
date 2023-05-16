from rest_framework.views import APIView
from django.contrib.auth.models import User 
from app.api.serializers import LoginSerializer, TodoListSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from app.models import Todo
from rest_framework import generics, permissions


class LoginAPIView(APIView):
    def post(self, request):
        data = request.data 
        serialize = LoginSerializer(data=data)
        # serializer bize hansi datalar gelecekse onu gosterir bize lazim olacaqlari
        if serialize.is_valid():
            # onlari yoxlayacaq bizim sertlerimize uygundurmu deye yeni her ikisi de gonderildimi 
            # typler dogrudurmu 
            # bu sertleri yoxlayir dogrudursa kecir ifin icine

            username = serialize.validated_data.get("username")
            password = serialize.validated_data.get("password")
            # burda serialize etmisik 15 ci setirde
            # hemin serialize arxada calisir ve bize dictionary qaytarir
            # hemin dictionary icinden username passwordu aliriq

            user = authenticate(username=username, password=password)
            # burda auth edirik yene basa dusmediz ? xeyr aydin oldu  birde yuxarida olan request.data js den gelen datadi ? beli jsdan post atarken gelen data(json formada gonderdik)
            # siz Alper Akbas in derslerini izleyin yene de belke orda tam aydin ola
            # hee yaxsi cox sagolun vaxtinizi aldim xosdur buyurun 
            if user is None:
                return Response(data={
                    "message":"User yoxdur."
                }, status=status.HTTP_404_NOT_FOUND)
            else: 
                refresh = RefreshToken.for_user(user)
                return Response(data={
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user_id':user.id
                })
           
        else : return Response(data={
            "message":"Invalid data."
        }, status=status.HTTP_400_BAD_REQUEST)
   

class TodoListAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated] # yeni login oldusa datani goster

    """

    Indi bu url=http://localhost:8000/auth/todos/ e get sorgusu atanda 
    access tokeni de gondermelisen ki
    access token tesdiqleyecek ki login olub 
    onda sene todo datani qaytaracaq 
    indi onu harda yoxlayaq
    loogin oldun access qaytardi
    sonra bu urle accessi atmalisan get sorgusu ile
    postman yukleyin sonra qosulub onu da gostererem ya da js ile ozunuz yoxlayin day orasi jsa qalib
    basa dusmediyim meselerden birde class based viewlardan istifade etmeden yazmaq olmaz ?
    Olar niye olmur ki sadece tez gosterdim 
    Alper Akbas
    Youtube de bu muellim 3 bolumluk drf dersleri var. izleyin onu 
    siz orada login serilazie ile login yoxladiz meselen onu enenevi usul ile yoxlayib etmekle ferqi nedir
    sual tam deqiq anlamadim ama bele deyim de
    Bele deyim
    serializer bizimcun json data qebul etdi ye onu bizim pythonun basa dusduyu oobyekte ceviri
    men cox vaxt orda baxanda daha yaxsi basa dusmek ucun function based viewlarda eliyirem bunun mene menfisi var yoxsa class based etmeliyem xeyr function larla class lar arasinda yazma vaxti meseleniz var de kodlari cox tekrarlayassiz boyuk bir e commerce yazasi olsaz class lar ile tez hell etmek olur 
    onda sizin etdiyiniz prosesi tekrar edib qisa formda size catdirim ki  gorum duz basa dusmusem 
    1- Siz loginserialize adinda class dan istifade ederek auth etdiz ve 
    auth u eden serialize deyil
    serialize etmek o deyil 
    men serializer ile javascriptden data aliram ve pythonun basa dusduyu formaya obyekte cevirirem
    authu normal django viewlarda nece idise ocur etdim
        """