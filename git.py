data_panen ={
    'lokasi1' :{
        'nama_lokasi' : 'kebun A',
        'hasil_panen' :{
            'padi'    : 1200,
            'jagung'  : 800,
            'kedelai' : 500,
        }
    },
    'lokasi2' :{
        'nama_lokasi' : 'kebun B',
        'hasil_panen' :{
            'padi'    : 1500,
            'jagung'  : 900,
            'kedelai' : 450,
        }
    },
    'lokasi3' :{
        'nama_lokasi' : 'kebun C',
        'hasil_panen' :{
            'padi'    : 1100,
            'jagung'  : 750,
            'kedelai' : 600,
        }
    },
    'lokasi4' :{
        'nama_lokasi' : 'kebun D',
        'hasil_panen' :{
            'padi'    : 1300,
            'jagung'  : 850,
            'kedelai' : 550,
        }
    },
    'lokasi5' :{
        'nama_lokasi' : 'kebun E',
        'hasil_panen' :{
            'padi'    : 1400,
            'jagung'  : 950,
            'kedelai' : 480,
        }
    }
}

<<<<<<< HEAD
# no 1

for i,j in data_panen.items():
    print (f'lokasi              : {i}')
    print (f'nama lokasi         : {j['nama_lokasi']}')
    print (f'hasil panen padi    : {j['hasil_panen']['padi']}')
    print (f'hasil panenjagung   : {j['hasil_panen']['jagung']}')
    print (f'hasil panen kedelai : {j['hasil_panen']['kedelai']}\n')

# no 2

data_panen2= data_panen['lokasi2']['hasil_panen']['jagung']
kebun2= data_panen['lokasi2']['nama_lokasi']
print(f'hasil panen jagung di {kebun2} adalah : {data_panen2}\n')

# no 3

lokasi= data_panen['lokasi3']['nama_lokasi']
print(f'nama lokasi dari kebun ke 3 adalah : {lokasi}\n' )

# no 4

padi1=data_panen['lokasi1']['hasil_panen']['padi']
padi2=data_panen['lokasi2']['hasil_panen']['padi']
padi3=data_panen['lokasi3']['hasil_panen']['padi']
padi4=data_panen['lokasi4']['hasil_panen']['padi']
padi5=data_panen['lokasi5']['hasil_panen']['padi']

kedelai1=data_panen['lokasi1']['hasil_panen']['kedelai']
kedelai2=data_panen['lokasi2']['hasil_panen']['kedelai']
kedelai3=data_panen['lokasi3']['hasil_panen']['kedelai']
kedelai4=data_panen['lokasi4']['hasil_panen']['kedelai']
kedelai5=data_panen['lokasi5']['hasil_panen']['kedelai']

print(f'Padi 1 : {padi1}   keledai 1 : {kedelai1}')
print(f'Padi 2 : {padi2}   keledai 2 : {kedelai2}')
print(f'Padi 3 : {padi3}   keledai 3 : {kedelai3}')
print(f'Padi 4 : {padi4}   keledai 4 : {kedelai4}')
print(f'Padi 5 : {padi5}   keledai 5 : {kedelai5}\n')

# no 5

padi = [
    data_panen['lokasi1']['hasil_panen']['padi'],
    data_panen['lokasi2']['hasil_panen']['padi'],
    data_panen['lokasi3']['hasil_panen']['padi'],
    data_panen['lokasi4']['hasil_panen']['padi'],
    data_panen['lokasi5']['hasil_panen']['padi']
]

kedelai = [
    data_panen['lokasi1']['hasil_panen']['kedelai'],
    data_panen['lokasi2']['hasil_panen']['kedelai'],
    data_panen['lokasi3']['hasil_panen']['kedelai'],
    data_panen['lokasi4']['hasil_panen']['kedelai'],
    data_panen['lokasi5']['hasil_panen']['kedelai']
]

total_padi=sum(padi)
total_kedelai=sum(kedelai)

print(f'jumlah seluruh padi adalah : {total_padi}\njumlah seluruh kedelai adalah : {total_kedelai}\n')

# no 6

for i,b in data_panen.items():

    padi   = b ['hasil_panen']['padi']
    jagung = b ['hasil_panen']['jagung']

    if padi > 1300 or jagung > 800 :
        print(f'{b}     :  memerlukan perhatian khusus\n')
    else:
        print(f"{b}     :  dalam batas aman\n")

print('221')
print('11291')