from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

#GET Data
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all() #ดึงข้อมูลจาก model Todolist
    serializer = TodolistSerializer(alltodolist,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# POST Data (save data to database)
@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



# PUT Data
@api_view(['PUT'])
def  update_todolist(request, TID):
    # localhost:8000/api/update-todolist/13
    todo = Todolist.objects.get(id=TID)

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



# PUT Data
@api_view(['DELETE'])
def delete_todolist(request, TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST

        return Response(data=data, status=statuscode)

    



data = [
        {
            "title":"Banana cake",
            "subtitle":"เค้กกล้วยหอมแป้งข้าวโอ๊ตสูตรคลีน100% แต่ยังคงความหอมอร่อยเหมือนร้านดัง",
            "image_url":"https://raw.githubusercontent.com/Maylomi/BasicAPI/main/banana-cake.jpg",
            "detail":"ส่วนผสม\n1.แป้งข้าวโอ๊ต / ข้าวโอ๊ตบดละเอียด 3 ช้อนโต๊ะ\n2.ไข่ 1 ฟอง\n3.ผงฟู / เบรกกิ้งโซดา 1/2 ช้อนชา\n4.น้ำผึ้งตามใจชอบ\n5.โปรตีนจากพืช 2 สกู๊ป\n6.กล้วยหอมสุกบด (แช่ตู้เย็นไว้จะทำให้สีสวยขึ้น) 1 -2 ลูก\n\nวิธีทำ\nผสมทุกอย่างเข้าด้วยกัน อบ 200 องศา 20 นาที"
            
        },
        {
            "title":"Pan cake",
            "subtitle":"แพนเค้กผลไม้ ของว่างทำง่าย แคลลอรี่ต่ำ",
            "image_url":"https://raw.githubusercontent.com/Maylomi/BasicAPI/main/pancake.jpg",
            "detail":"ส่วนผสม\n1.แอปเปิ้ล​ 2 ลูก\n2.กรีกโยเกิร์ต​หรือโยเกิร์ต​รส​ธรรมชาติ​ก็ได้ 1 ช.ต\n3.นำ้มันมะพร้าว 1 ช.ต(หรือนำ้มันพืช)\n4.ไข่ 1 ฟอง\n5.ข้าว​โอ๊ต​ปั่น​ละเอียด​ 8 ช.ต\n6.กลิ่นวานิลลา​ครึ่งช้อนชา(ไม่มีไม่ต้อง)\n7.เกลือสีชมพู​+เบ็ค​กิ้​ง​โซดา​อย่างล่ะหยิบมือ(ไม่ชอบ​ไม้ต้อง)\n8.ท้อปปิ้งตามชอบ\n\nวิธีทำ\nปอกเปลือก​แอปเปิ้ล​ หั่นชิ้นเล็กชิ้นน้อยแล้วนำมาปั่นกับส่วนผสม​ข้อ2-4ให้ละเอียด ตามด้วย​ส่วนผสม​ที่เหลือปั่นให้เข้ากันอีกที ตั้งกระทะไปกลางค่อนข้าง​อ่อน​ ทาน้ำมันมะกอก​บางๆที่กระทะ​ รอกระทะ​ร้อน ตักแป้งทีละ2ช้อน ลงทอดลงสุกทั้ง2ด้าน ตกแต่งด้วยผลไม้และไซรัปตามชอบ พร้อมเสิร์ฟ"
        },
        {
            "title":"Coffee oat cookies",
            "subtitle":"คุกกี้ข้าวโอ๊ตกาแฟ คุกกี้หอมกรุ่นเหมาะสำหรับยามเช้าพร้อมอัดแน่นไปด้วยโปรตีนจากธัญพืช",
            "image_url":"https://raw.githubusercontent.com/Maylomi/BasicAPI/main/oat-cookies.jpg",
            "detail":"ส่วนผสม\n1.ข้าวโอ๊ตแบบเต็มเมล็ด  200 กรัม\n2.ไข่ไก่ 2 ฟอง\n 3.กาแฟฟรีซดราย 1 ชต\n4.น้ำตาลทราย 70 กรัม\n5.น้ำมันมะพร้าวหรือน้ำมันรำข้าว 100 กรัม\n 6.แป้งข้าวโพด 2 ชต\n7.ผงฟู 5 กรัม(2 ชช.)\n8.วนิลลา 1/2ชช\n 9.ผลไม้แห้งเช่น ลูกเกด แอปพริคอต หรือถั่วหรืออัลมอนด์บุบ รวมกันหรืออย่างใดอย่างนึงตามชอบ ออกแบบได้เลยค่ะ ใส่ได้ถึง 100 กรัม\n\n วิธีทำ\n1.นำไข่/ผงกาแฟ/น้ำตาลทราย/น้ำมันพืช /วนิลลา คนผสมให้เข้ากัน\n2.เติมข้าวโอ๊ต /แป้งข้าวโพด/ผงฟู ผสมทั้งหมดให้เข้ากัน\n3.เติมผลไม้แห้งและถั่ว ผสมให้เข้ากันดี\n4.ตักใส่ถาด จะใช้ช้อนหรือscoop ตัก แต่งหน้าด้วยช็อกโกแลตชิพ อบด้วยไฟ170องศา ประมาณ 15นาที แล้วลดไฟลง150 อบต่อ20-30 นาที\n5.เมื่อออกจากเตาจะนิ่ม ต้องทิ้งไว้ให้เย็นจึงค่อยแซะออก และคุกกี้จะกรอบเมื่อเย็นตัว"
        },
        {
            "title":"Strawberry tart yogurt",
            "subtitle":"อากาศร้อนๆมาทำทาร์ตโยเกิร์ตสตรอเบอรี่กันดีกว่า สดชื่นแบบไม่กลัวอ้วน",
            "image_url":"https://raw.githubusercontent.com/Maylomi/BasicAPI/main/cheese-cake.jpg",
            "detail":"ส่วนผสมแป้งทาร์ต\n1.แป้งอัลมอนด์ 6 ช้อนโต๊ะ\n2.แป้งข้าวโอ้ต 6 ช้อนโต๊ะ\n3.เนยจืดแท้ 35กรัม ใช้เนยเค็มตัดเกลือข้างล่างออก\n4.น้ำตาลอิริทอล 1ช้อนโต๊ะ\n5.เกลือ 1/4ช้อนชา\nส่วนผสมครีมโยเกิร์ต\n1.โยเกิร์ต รสธรรมชาติ 1ถ้วย\n2.น้ำเปล่า 50 ml\n3.ผงวุ้น 1/4 ช้อนชา\n4.ผงเจลลาติน 1/2 ช้อนชา\n5.น้ำตาลอิริทอล 2 ช้อนโต๊ะ\nส่วนผสมซอสสตรอเบอร์รี่\n1.น้ำเปล่า 100ml\n2.สตรอเบอร์รี่ แช่แข็ง 50g\n3.ผงวุ้น 1/4 ช้อนชา\n4.ผงเจลลาติน 1/2 ช้อนชา\n5.น้ำตาลอิริทอล 4 ช้อนโต๊ะ\n\nวิธีทำ\n1.เทแป้งแล้วคนให้เข้ากัน ตามด้วยเนย เกลือ และน้ำตาล คนให้เข้ากัน แล้วขยำนวดด้วยมือ (สังเกตุแป้ง จะปั้นเป็นก้อนกลมๆได้ไม่แตก หากแตกให้เพิ่มแป้งข้าวโอ้ตทีละน้อยแล้วสังเกตุ)\n2.แผ่แป้งให้แบนๆ บนแผ่นพลาสติกใส แล้วห่อ (ถ้าแผ่ได้แบน จะได้2ถาด) แช่ตู้เย็น 1ชั่วโมง\n3.เตรียมครีมโยเกิร์ต : นำน้ำเข้าไมโครเวฟให้ร้อนจัดเทผงวุ้นคนให้ละลายตามด้วยเจลลาตินคนให้ละลาย เทน้ำตาลแล้วคนให้ละลายตามด้วยโยเกิร์ตคนให้เข้ากัน รอให้คลายร้อนจึงนำแช่ตู้เย็นให้เซ็ตตัวประมาณ 30นาที\n4.เตรียมซอสบลูเบอร์รี่ : ตั้งน้ำให้เดือด ใส่บลูเบอร์รี่แล้วเคี่ยวให้นุ่มเล็กน้อยตามด้วยน้ำตาล เคี่ยวต่อให้น้ำงวดเติมผงวุ้นและเจลลาติน คนให้งวดอีกทำประมาณ 15นาทีใช้ไฟอ่อน\n5.นำแป้งทาร์ตออกจากตู้เย็น ตัดให้เท่าถาดนำวางในถาดใช้ส้อมเจาะรูให้ทั่ว นำเข้าหม้อทอดไร้น้ำมัน 170c, 15นาที นำออกจากเตาพักให้เย็นลง\n6.เทครีมโยเกิร์ตลงในแป้งทาร์ตแล้วนำไปแช่เย็นให้ครีมโยเกิร์ตเซ็ตตัว 2ชั่วโมง (แช่ข้ามคืนยิ่งดี)\n7.นำแป้งทาร์ตที่ครีมโยเกิร์ตเซ็ตตัวดีแล้วออกจากตู้เย็น แล้วเทซอสลงในถาด พร้อมเสริฟ"
        },
        {
            "title":"Brownie",
            "subtitle":"บราวนี่เนื้อนุ่มรสเข้มข้นถึงใจ โปรตีนสูงงงงงงง",
            "image_url":"https://raw.githubusercontent.com/Maylomi/BasicAPI/main/chocolate-brownies.jpg",
            "detail":"ส่วนผสม\n1.ถั่วแดงต้ม 80 กรัม\n2.ไข่ไก่ 3 ฟอง\n3.น้ำตาลมะพร้าว ออแกนิค 80 กรัม\n4.ผงฟู1 ชช\n5.ผงโกโก้ 2 ชช\n6.นม 2 ชต\n7.เวย์โปรตีนรสช็อคโกแลต 1 สคูป\n\n วิธีทำ\nผสมทุกอย่างเข้าด้วยกัน จากนั้นนำไปปั่นในโถปั่นให้ละเอียด เทใส่พิมพ์ เข้าเตาอบไฟบนล่าง 170 องศาเซลเซียส 35 นาที"
            
        }
    ]


def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii': False})
