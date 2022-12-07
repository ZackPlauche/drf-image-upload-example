# How To Upload An Image to DRF Using Fetch API


## Minimal Requirements

### Packages
- `django`
- `djangorestframework`
- `django-cors-headers`
- `Pillow`

Convenience command
```cmd
pip install django djangorestframework django-cors-headers Pillow
```

### Settings
```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'corsheaders'    
    # ...
]

MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    #...
]



# Media settings (determines where images will be uploaded)

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

# Cors (determines which urls can access your data. Only required for browser access)

CORS_ALLOW_ALL_ORIGINS = True  # Not required, but convenient for testing
```

### config/urls.py

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
]

if settings.DEBUG:
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

<!-- // const createImage = async (event) => {
//   event.preventDefault()
//   if (imageInput.value) {
//     let formData = new FormData()
//     let imageFile = imageInput.files[0]

//     formData.append(imageFieldName, imageFile)

//     let newImage = await fetch(imageEndpoint, {
//       method: 'POST',
//       body: formData  // Form Data automatically takes care of the correct content-type with the proper "boundary" setting
//     })
//       .then(response => response.json())
//       .catch(error => { console.error(error)})
//     imageInput.value = ''
//     addImageToList(newImage)
//   } else {
//     alert('No Image selected.')
//   }
// } -->

const imageInput = document.querySelector('input')
const imageList = document.querySelector('#imageList')

const imageFieldName = 'file'  // Determined in by your Model with an ImageField or FileField (e.g., BlogPost.image <- Would be 'image')