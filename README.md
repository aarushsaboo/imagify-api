here's the curl request to \predict


Invoke-RestMethod -Method Post -Uri 'https://api.cortex.cerebrium.ai/v4/p-fa725bb1/firstproject/predict' -Headers @{ 'Content-Type'='application/json'; 'Authorization'='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0SWQiOiJwLWZhNzI1YmIxIiwiaWF0IjoxNzQzNTIzMTE2LCJleHAiOjIwNTkwOTkxMTZ9.wKirJOC_9HyyGyhcHv5Won52qqbaeSNvt2d1uiy4OYrc-eg0DrabuxyyC5m7OWIxqgJEgSBoPFNQ5tj5f3dnijIDpyjAy4i5DOxCMMCPn35wwwhuVmkqBSodsJ5dg2Wj6Fz-Sir23F3SXObYM6UWEHfSM8EyaF5q62pQh9e9dVdyJD7j27620xuehpXLA4hFQld7xHwG7rbpUIbMgROmElIMNNIgvjUIfdJ5uBg9ZZLL8jje9VNrmdT31nIPP-Q_VrnrAyF6WHPHrRTfIPgOLr1m2r6O4zzEEpyTVu3QWEJq9hQSuGtG0V00PBJldpd3EnL330kL_Jqq4CfRdfz5tg' } -Body (@{ 'prompt'='test image' } | ConvertTo-Json) -ContentType 'application/json'
