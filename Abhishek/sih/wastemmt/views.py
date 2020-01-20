from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import images
from .models import logcredential
from django.core.files.storage import FileSystemStorage
# Create your views here.

def checktype(v):
    v=list(v)
    val=[]
    for i in range(len(v)-3,len(v),1):
        val.append(v[i])
    val="".join(val)
    return val
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def sample(request):
    return render(request,'sample.html')

def upload(request):
    if request.method=='POST':
        uploadedfiles=request.FILES['imgfile']
        fs=FileSystemStorage()
        fs.save(uploadedfiles.name,uploadedfiles)
        allproducts = images.objects.all()
        ProdName = (images.objects.values("garbageimage"))
        print(ProdName)
    return render(request,'map.html')

def signup(request):
    if (request.method == "POST"):
        username = request.POST.get('userkanaam')
        password = request.POST.get('userkapassword')
        data=logcredential(usernames=username,passwords=password)
        data.save()
    return render(request, 'home.html')

def signin(request):
    if (request.method == "POST"):
        username = request.POST.get('userkanaam2')
        password = request.POST.get('userkapassword2')
    allproducts = logcredential.objects.all()

    user=(logcredential.objects.values("usernames"))
    pwd=(logcredential.objects.values("passwords"))
    user=[items['usernames'] for items in user]
    pwd=[items['passwords'] for items in pwd]

    #checking for correct entry

    for i in range(len(user)):
        if(user[i]==username and pwd[i]==password):
            return render(request,'index.html')
    return render(request,'map.html')



        # data=logincredentials(usernameslogin=username,passwordslogin=password)
        # data.save()


def map(request):
    # allproducts = images.objects.all()
    # ProdName=(images.objects.values("garbageimage"))
    # prodName=[ items['garbageimage'] for items in ProdName]
    # params={'allprods':allproducts}
    # typesoffiles=checktype(prodName[1])
    return render(request, 'map.html')

    # integrating latitude longitude from images

    from PIL import Image
    def get_exif(filename):
        image = Image.open(filename)
        image.verify()
        return image._getexif()

    from PIL.ExifTags import TAGS

    def get_labeled_exif(exif):
        labeled = {}
        for (key, val) in exif.items():
            labeled[TAGS.get(key)] = val

        return labeled

    exif = get_exif("Screenshot_19.png")
    labeled = get_labeled_exif(exif)

    from PIL.ExifTags import GPSTAGS

    def get_geotagging(exif):
        if not exif:
            raise ValueError("No EXIF metadata found")

        geotagging = {}
        for (idx, tag) in TAGS.items():
            if tag == 'GPSInfo':
                if idx not in exif:
                    raise ValueError("No EXIF geotagging found")

                for (key, val) in GPSTAGS.items():
                    if key in exif[idx]:
                        geotagging[val] = exif[idx][key]

        return geotagging

    geotags = get_geotagging(exif)

    def get_decimal_from_dms(dms, ref):

        degrees = dms[0][0] / dms[0][1]
        minutes = dms[1][0] / dms[1][1] / 60.0
        seconds = dms[2][0] / dms[2][1] / 3600.0

        if ref in ['S', 'W']:
            degrees = -degrees
            minutes = -minutes
            seconds = -seconds

        return round(degrees + minutes + seconds, 5)

    def get_coordinates(geotags):
        lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

        lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

        return (lat, lon)

    exif = get_exif("Screenshot_19.png")
    geotags = get_geotagging(exif)
    print("oooooooooooooooooooooooooooooooppppppppppppp",get_coordinates(geotags))

    #end of integration
    return render(request,'map.html',params)

# def getlocation(request):
#
def sample(request):
    return render(request,"sample.html")
