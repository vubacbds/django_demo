#cài python thì lên gg tải về
#xong mở cmd chạy lên tenfile.py, hoặc python tenfile.py
#khác là có thêm module có sắn để import 
  #hoặc module tự viết nhưng chỉ gọi khi cùng thư mục 
  #khác thư mục thì dùng Package
  #phải xử lý đa luồng
#chuỗi với list,.. có vị trí trái sang phải là 0 đến length-1, phải qua trái là từ -1 đến - số nào đó
#python dành cho ai muốn code ngắn gọn vì hỗ trợ nhiều thư viện sẵn
#các khối code thì thụt vào 4 spcace, hoặc từ : nhấn enter
#các biến trong hàm là local, để toàn cục thêm global
#editor viết dùng sublimetext, chạy lên bằng ctrl+B
#Cách định dạng code html python trên vs-code
  #1. Mở file setting.json: file >> preferent >> setting >> icon phía trên bên phải có dấu mũi tên và trang giấy
  #2. cài extention Beautify và thêm code vào file json trên, xem code tại đây : https://stackoverflow.com/questions/42170561/vscode-html-autoformat-on-django-template
 #Cách auto thẻ đóng trên html django vscode 
  #1. cài extention Auto close tag 
  #2. thêm đoạn code xem trong đây: https://stackoverflow.com/questions/61744003/how-can-i-autocomplete-both-html-and-django-html-simultaneously-in-visual-studio

####----- Chuỗi----- ################################
print("hello world")

a = 'bac'
#kiểu dữ liệu
print(type(a))

#kiểu int thì vô hạn, 
#kiểu float thì chỉ lấy 15 chữ số thập phân

from decimal import*
#kiểu decimal lấy tối đa 30 chữ số cả phần nguyên và thập phân
getcontext().prec = 30
print(Decimal(10)/Decimal(3))

from fractions import*
#phân số
frac = Fraction(6,9)
print(frac)

#số phức
c = complex(2,5)
print(c)

#chia lấy phần nguyên
print(10//3)

#chia lấy phần dư
print(10%3)

#lũy thừa
print(2**2)

#Ngoài ra thư viện math có các hàm toán học
#Chuỗi xuống hàng
d = 'vu \n xuan bac'
#Cho mọi thứ bên trong đều là chuỗi
e = r'vu \n xuan bac'
#dùng biến trong chuỗi
ff = 'dt'
f = f'vu xuan bac {ff}'
print(f)
#để có kí tự dấu nháy trong chuỗi
g = 'vu \" xuan bac'
print(g)
#dùng chuỗi link hoạt vị trí
#ngoài thay thế chuỗi còn có số, vv...
h = '%s vu xuan bac la %s %.2f' %('tên','tôi', 1.2345)
print(h)

#dùng format 
i = '{}, {}, {}'.format('one', 'true', 'three')
print(i)
#nếu để số vào thì sẽ thay đổi vị trí
i2 = '{1}, {0}, {2}'.format('one', 'true', 'three')
print(i2)

#căn lề, ^ giữa, < trái, > phải, 20 ký tự dùng dấu - để thế chỗ phần trống
strC = '{:-^20}'.format('vuxuanbac')
print(strC)


#cho chuỗi lặp nhiều lần
strA = 'vuxuanbac'
strB = strA*4
print(strB)
#chuỗi có tồn tại trong chuỗi
print('c' in strA)
#lấy các kí tự trong chuỗi
print(strA[1])
#số - thì lấy từ phải sang trái bắt đầu từ -1
print(strA[-1])

#cắt chuỗi, bên trái : là là từ vị trí đó, bên phải : là đến vị trí đó trừ đi 1
print(strA[0:3])
#None là các ký tự còn lại
print(strA[1:None])

#cắt chuỗi có bước nhảy 2
print(strA[0:None:2])

#ép kiểu 
strC = float('6.9')
print(strC)
numA = str(12)
print(numA)

#đầu các từ viết hoa, thủ thuật là mã chữ thường trừ đi 32 ra chữ hoa
strD = 'vu xuan bac'
print(strD.title())
#căn lên giữa, rjust là phải, ljust là trái
print(strD.center(30, '-'))

#thay thế chuỗi
strE = 'vũ xuân bắc'
print(strD.replace('u', 'p'))
#thay thế bao nhiêu lần , số âm thì lấy từ phải sang
print(strD.replace('u', 'p', 1))

#bỏ các khoảng trắng, hoặc 1 ký tự nào đó, lstrip là bên trái, rstrip là bên phải
strF = '  vũ xuân bắc   '
print(strF.strip())

#cắt chuỗi thành list
strG = 'vũ xuân bắc'
print(strG.split(' '))

#cắt có số lượng thì thêm số vào, rsplit là từ phải, lsplit bên trái
strI = 'vũ xuân bắc'
print(strI.split(' ', 1))

#kiểm tra ký tự có ở đầu chuỗi
strK = 'vu xuan bac'
print(strK.startswith('v'))

#kiểm tra ký tự ở đầu chuỗi tại 1 vị trí
strK = 'vu xuan bac'
print(strK.startswith('u', 1))

#tìm chuỗi với find, trả về vị trí, nếu ko thấy trả về -1
strL = 'vu xuan bac'
print(strL.find('b'))
#tìm phải qua là rfind, trái là lfind

#tìm chuỗi với index, khác find là tìm ko thấy sẽ lỗi
strL = 'vu xuan bac'
print(strL.index('c'))

#kiểm tra phải chuỗi số ko
strM = '123'
print(strM.isdigit())

#kiểm tra chuỗi tất cả là khoảng trắng dùng isspace

#### --- LIST ---- ################################
#có khả năng chứa mọi kiểu và cả list con
#tạo ra 1 list từ vị trí 0 đến 30-1
liA = [i for i in range(30)]
print(liA)

#tạo ra 1 list từ một vị trí nào đó đến 10-1
liB = [i for i in range(1, 10)]
print(liB)

#tạo ra 1 list clone với constructor list
#vì nếu dùng gán list cho biến khác thì khi biến khác thay đổi thì list cũ cũng bị đổi
#tuy nhiên dùng clone list thì cũng ko clone dc các list con bên trong
cloneA = list([1,2,3])
#tạo 1 list với các phần tử là các ký tự của chuỗi
cloneB = list('vuxuanbac')
print(cloneB)
#cắt list như chuỗi
print(cloneA[1:3])

#hàm đếm số lần xuất hiện
cloneC = [1,1,1,2,3,4]
print(cloneC.count(1))
#tìm vị trí cũng là index như chuỗi, ko có find
#ngoài clone bằng list có thể clone bằng hàm copy()
print(cloneC.copy())
#clear để xóa hết phần tử list
#append thêm phân tử vào list
  #chỉ truyền dc 1 ký tự
cloneD = [1,2,3]
cloneD.append(4)
print(cloneD)
#extend thì giải [] chỉ lấy ra các phần tử list con và thêm vào
cloneD.extend([4,5])
print(cloneD)

#insert thêm một phần tử vào vị trí nào đó
  #thêm 12 vào vị trí 1
cloneD.insert(1,12)
print(cloneD)

#pop là xóa đi phần tử truyền vào vị trí trong list và trả về phần tử xóa đó
cloneD2 = cloneD.pop(0)
print(cloneD2)

#remove cũng xóa truyền vào giá trị và ko trả về phần tử
#reverse ra một list đảo ngược lại
#sort để sắp xết lại list, mặc định nhỏ tới lớn, và phải cùng kiểu dữ liệu
  #truyền vào reverse=true/false để sắp xếp lại

#### --- TUPLE ---- ################################
  #tốc độ truy xuất nhanh hơn và dung lượng bộ nhớ nhỏ hơn list
  #bảo vệ dữ liệu ko bị thay đổi
  #có thể dùng làm key của kiều dict
  #trường hợp (1) là int ko phải tuple
  #clone tuple bằng tuple()

#cách tạo 1 tuple nhanh
#ko có phần tử ngay như list
tup = (i for i in range(10) if i%2 == 0) 
#thêm bước này để có phần tử
tupA = tuple(tup)  
print(tupA)

#tuple giống chuỗi là hashable obj ko thể thay đổi, còn list là unhashable  obj
  #hash obj thì máy tính chỉ cấp đủ bộ nhớ thôi 
     #nên là khi thay vào thì nó chuyển sang ô nhớ khác, có địa chỉ khác
#tuy nhiên phần tử con của tuple là list thì thay đổi dc
#tuple ko có hàm append chỉ có toán tử +=
  #khi dùng += như thế thì máy tính phải đi vòng để tìm ô nhớ chứa nó
  #hàm id() trả về địa chỉ ô nhớ dạng số int và ko đổi trong quá trình chạy
    #trừ khi thay đổi ô nhớ
    #ví dụ như List hay Set là unhashable có thể thay đổi và bộ nhớ còn khoảng trống 
      #nên khi id() sẽ ko thay đổi


#### --- SET ---- ################################
#set ko chứa phần tử trùng lặp
#chỉ chứa các hashable obj nhưng chính nó ko phải là hashable obj nên cũng ko thể thay đổi
  #phần tử cháu/chắt là unhashable cũng ko thể chứa
#nếu set là trống {} thì lại trở thành kiểu dict
set_1 = {1,2}
print(set_1)

#tạo set clone, có thể truyền vào list,vv...
#có thể tạo set trống bằng set() luôn
set_2 = set(('a','b','c'))
print(set_2)

#toán tử - : lấy cái của bên trái mà bên phải ko có
#toán tử & : cả 2 thằng đều có
print({1,2,3,4} & {4,5})
#toán tử | : lấy tất cả mà trùng thì lấy một
#toán tử ^ : lấy hết tất cả của 2 bên nhưng loại trừ cái bị trùng nhau của 2 thằng
  #hoặc ^ = | - &

#index hay cắt set ko dc hỗ trợ
#hàm cơ bản như clear, pop() : xóa và lấy ra thằng đầu tiên
#remove thì truyền vào giá trị và xóa
#discard thì cũng như remove khác là ko có giá trị đó nó ko báo lỗi
#hàm copy() để clone, add() thì thêm nếu trùng thi ko thêm dc

#### --- DICT ---- ################################
#comprehension là cái tạo list/tuple/set/dict nhanh
#iterable này đặc biệt hơn, iterable khác thì là list/tuple/set
iter1 = [('name', 'bac'), ('member', '68')]

#constructor dict
dictA = dict(iter1)
print(dictA)

#dùng dict() để tạo dict thì key ko cần là chuỗi
  #nếu trùng tên biến bên ngoài cũng ko ảnh hưởng gì
 
#tạo dict từ iterable thường
iter2 = ('name', 'age')
#fromkeys() là các phầng tử của iter trên làm khóa, nếu có tham số thứ 2 thì là gán giá trị mặc định
dictB = dict.fromkeys(iter2, 'ok')
print(dictB)

#lấy value của dict
print(dictB['name'])
#gán giá trị
dictB['name'] = 'bac'
print(dictB)
#nếu gán giá trị cho dict với 1 key ko tồn tại thì nó tự thêm vào
dictB['high'] = '168'
print(dictB)

#sửa value
dictB['name'] = dictB['name'] + ' vu xuan'
print(dictB)

#hàm copy() tạo bản sao dict mới
#gọi value qua hàm get(key) 
  #ko có key thì trả về none
  #ko có key và có tham số thứ 2 thì ra giá trị mặc định
dictC = dictB.get('friend', 'no')
print(dictC)

#hàm items() trả về và đổi về list các giá trị 
dictD = list(dictB.items())
print("tes+++++++++++++++++++++")
print(dictD)

#lấy ra các key
print(dictB.keys())
#lấy ra các value
print(dictB.values())

#pop() để xóa và đồng thời trả về giá trị xóa (lấy ra luôn)
  #nếu tham số pop ko có key nào trùng mà có default thì ko bị lỗi

#setdefault() thì truyền key vào để lấy value, nếu ko có key thì nó tạo mới với key là tham số đó , và value là none
#update()
dictL = {'n': '1', 'm':'2'}
print(dictL)
dictL.update(n='dung')
print(dictL)

#######----xử lý file---####
#cùng cấp với file .py chạy
#mở với open(), tham số 1 là tên file, tham số 2 là mode, r đọc, r+ ghi, w ghi mất dữ liệu cũ, w+ ghi đọc, a và a+

#mở file
file_object = open("a.txt", "r")
#đọc với read(), tham số là vị trí đọc tới
data = file_object.read()
print(data)
#đóng vì đọc tới đâu con trỏ tới đó, đọc lại ko còn dữ liệu
   #hoặc thì dùng hàm seek(0) để quay lại con trỏ về 0
file_object.close()

#readline : đọc từng dòng, readlines thì đọc từng dòng và chuyển đổi thành list
#file cũng là iterable là như list/tuple nên dùng list(file)
#dùng with
  #with close luôn khi khối lệnh bên trong xử lý xong
with open("a.txt", "r") as fobj:
     d = fobj.read()
print(d)

####-------Iteration----####
#Iteration là cái gì dùng vòng lặp và có thể lấy giá trị 
#iterable là 1 obj có phương thức __iter__ và phường thức __getitem__
  #như list, chuỗi, 
#iterator obj là chỉ lấy giá trị của từng phần tử qua hàm next(iter)
 #tạo iterator qua ( i for i in rang(30))
 #tuple là iterator
 #hàm next(iter) để lấy giá trị dùng trong vòng lặp while
#các hàm tính iterable
  #sum(iter, firstTotal)
  #max(iter, default)
  #min(iter, default)
  #sorted(iter, reverse=True/False) sắp xếp

####-----hàm xuất print----###
  #print() có các params như:
     #sep: thay khoảng cách khoảng trắng bằng ký tự nào đó
     #print('a' + 'b') nối chuỗi lại khác print('a','b') có khoảng trắng
     #end : mặc định là xuống dòng, có thể thay thế bằng ký tực khác mỗi khi print
       #khi có newline (xuống dòng) thì print mới hiện, ko thì nó cứ để bộ nhớ đệm, khi có newline nó in cả thể 1 lần
       #muốn xuất ra mà ko cần newline là thêm flush=true để xuất từ bộ nhớ đệm ra
     #file=file_obj thì print() nó viết vào file luôn
  #trong python 2.x print ko phải hàm, 3.x là hàm print()
#hàm sleep(), phải import vào từ from time


####-----hàm nhập input----###
# value = input('nhap vao di: ')
# print(f'gia tri vua nhap la {value}')

#raw_input tồn tại ở Python 2.x

#khác nhau giữa %s và %r
  #dùng 2 phương thức của class khác nhau
  #%r thì nếu là chuỗi nó thêm dấu '', số ko thêm dấu nháy
  #%s thì thành chuỗi trực tiếp luôn
chuoiA = "toi la %s" %(12)
chuoiB = "toi la %r" %(12)
print(chuoiA)
print(chuoiB)


###-----Kiểu Boolean-----####
#khác nhau giữa == và is 
  # == thì so sánh bằng giá trị
  # is thì dùng giá trị id() có nghĩa là địa chỉ ô nhớ về int
  # đặc biệt nếu số từ -5 đến 256 thì is vẫn true vì id() trả về cùng ô nhớ
  #ở python and có thể bỏ 
    #or thì dùng in với list

  ### if_else---#
  #Cả khối của if là đều thụt vào 1 tab
    #nên if có thể lồng nhau
  #Ỏ python, block là thụt vào trong, và bắt buộc phải có 1 dòng lệnh
    #nhưng ko phải kiểu tab hay cách mà từ dấu : phải nhấn enter mới được
    #hoặc cách ra 4space để thụt khối code
    #nếu ko enter xuống dòng/ cách vào 4 spce để tạo block thì có thể để cùng dòng nó cũng thành block


###while
#dùng break thì kết thục vòng lặp
#dùng continute thì vẫn chạy tiếp vòng lặp mà bỏ qua dòng code bên dưới nó
#nếu khai báo 1 biến bên ngoài vòng lặp while và xử lý nó trong while thì biến đó sẽ bị thay đổi
  #nếu như trong hàm thì cho dù trùng tên biến nó cũng chỉ là local nên biến bê ngoài ko bị thay đổi
  #thêm từ khóa global phía trước để thay đổi dc biến đó trong hàm

###---for loop ---###
#với kiểu dict
dict = {'name': 'bac', 'birt': 2000}
for name, key in dict.items():
  print(name, '=>' ,key)

#for else thì xong lặp chạy khối lệnh trong else
  #cũng có while else
  #nếu có break thì khối lệnh trong else cũng bỏ
#range() là class tạo ra dãy số
 #range() có 3 tham số là (start, stop, step)
   #range(12) nghĩa là start 0, stop 12, step 1
     #nó sẽ cho ra dãy số từ 0 đến 11 (nghĩa là 12 - step) chạy từ trái sang phải vì step dương
   #range(12,0,-1)
     #nó sẽ cho ra dã số từ 12 đến 1 (từ phải sang trái vì step âm)
#dùng range và indexing trong for loop để in ra các phần tử
  #dùng vậy để update list
lst = [5, (1,2,3), {'abc', 'xyz'}]
for i in range(len(lst)):
  print(f'Phần tử là: {lst[i]}')

#comprehension thay thế for loop sẽ ngắn hơn 1 dòng và tốc độ nhanh hơn
test1 = {key:value+1 for key, value in (('num1', 1), ('num2',2)) if value%2 == 0}
print(test1)

#enumerate thay cho range để lấy vị trí khi dùng for loop
student_list = ['bac', 'duong', 'linh']
gen = enumerate(student_list)
print(gen)
for index, value in gen:
  print(index, '=>', value)

#####-----Function
#nếu khối lệnh chưa biết gì để là 'pass' để ko lỗi
#hàm nếu muốn truyền thiết tham số thì thêm giá trị default cho nó
  #giá trị default có thể thay đổi
  def f(name=[]):
    name.append('F')
    print(name)
  f()
  f()
  f()
#có thể truyền tham số vào hàm 2 cách
  #truyền theo thứ tự như thường
  #truyền qua key là tên tham số của hàm đã định nghĩa, ko cần đúng vị trí
  #hoặc dùng cả 2 cái trên để truyền
def ll(a,b,c,d):
  pass
ll(12,'ok', d=0, c=1)
  
  #đối với 1 số cái thì bắt buộc phải có key 
print(sorted([3,4,1], reverse=True))
  #nếu có 1 tham số là dấu * nó chỉ có nghĩa là đánh dâu sau đó là các tham số chỉ truyền qua key 
     #tham số * này chỉ ở các phiên bản 3.5 trở xuống

#có cách giải list/tuple để truyền vào hàm

def f3(a,b,c,d):
  print(a,b,c,d)  
listG = [1,2,3,4]
#dùng dấu * để unpaking (giải mảng)
f3(*listG)

print('paking-------------------------------')
#để paking thì
def f4(*args):
  print(args)
f4(*(x for x in range(12)))
  #nếu như có tham số thứ 2 thì ko dc dùng paking và để gọi thì phải dùng key để thêm vào

#để unpaking với dict thì dùng ** và khi khai báo hàm phải truyền tham số đúng với tên key của dict
def f5(name, age):
  print('name', '=>', name)
  print('age', '=>', age)

dict5 = {'name': 'bac', 'age': 2000}
f5(**dict5)

#khi paking với dict thì chỉ cần ** với tham số truyền vào hàm
  #và các paking phải nằm trước các key tham số (nếu có)

  #biến global trùng tên với biến local thì sẽ ưu tiên local vì gần nhất với hàm đó
    #hạn chế dùng global vì làm code loạn lên

  #trong hàm dùng return dể trả về giá trị
    #sau return thì các dòng lệnh ko chạy
    #có thể return nhiều giá trị cách nhau bằng dấu phẩy

#generator là 1 dạng của iterable (kiểu khi tại tuple bằng range là ra cái này) 
  #ko lưu trữ toàn bộ vào bộ nhớ như interation mà sinh ra lần lượt, đè lên cái cũ
  #duyệt qua for loop
  #có thể thay return bằng yield
    # ví dụ trả về list thì với return sẽ trả về 1 list mới đã thay đổi các phần tử
      #yield thì ko cần mà tác động lên list cũ luôn
      #return thì sẽ dừng hàm luôn
      #yield thì khi gặp sẽ ngắt hàm và chạy lệnh bên dưới. rồi nếu hàm chạy tiếp mà còn yield nữa thì tiếp tục chạy hàm với yield tiếp theo mà yield cũ vẫn tồn tại
  #yield có thể coi là 1 return tạm thời
#khi dùng yield thì phải dùng for loop để duyệt, vì khi yield nó sẽ trả về generator
def gen():
  yield 'vu'
  print('yiled lần 2')
  yield 'xuan'
  print('yield lần 3')
  yield 'bac'

for value in gen():
  print(value)

#ngoài dùng for loop để duyệt thì có 1 số hàm hỗ trợ generator trong python
  #next(hàm generator)
  #sau đó dùng (hàm generator).send(truyền vào giá trị thì yield sẽ tiếp tục chạy)

print("---yield--------------------------------")
def gen2():
  while True:
    x = yield
    yield x ** 2
gg = gen2()
next(gg)
print(gg.send(2))
next(gg)
print(gg.send(10))
#dùng yield vì nhanh hơn, ko cần lưu tất cả các giá trị

#khai báo function khác với lamda - khác def tạo hàm với tên xác định thì lamda trả về hàm
#lamda tạo hàm trong 1 dòng lệnh, hoặc viết hàm trong hàm 1 cách nhanh chóng
#lamda dùng tạo hàm đơn giản
ave = lambda a,b,c: (a+b+c)/3
print(ave(1,3,2))
#dùng lambda làm các phần tử của list, là có nhiều hàm 
finde = lambda x,y: x if x>y else y
print(finde(1,2))

#các hàm map, filter có 2 tham số: thứ 1 là function, thứ 2 là interable như list/tuple..
 #reduce có 3 tham số: thứ 1 là function, thứ 2 là interable như list/tuple, thứ 3 là giá trị ban đầu (ko bắt buộc)
from functools import reduce
kt = lambda x,y: x+y
ktl = [1,2,3,4,5]
print(reduce(kt, ktl, 10))
   #nó sẽ cộng các số trong dãy lại từ đầu tới hết rồi cộng thêm giá trị ban đầu là 10

#đệ quy (hàm gọi lại trong nó, phải có điểm dừng ko nó vô tận)
def cal_sum(lst):
  if not lst: #tương đương if len(lst) == 0
    return 0
  else:
    return lst[0] + cal_sum(lst[1:])
print(cal_sum([1,2,3,4]))

#cách viết khác 
def cal_sum2(lst):
  return 0 if not lst else lst[0] + cal_sum(lst[1:])
print(cal_sum2([1,2,3,4,5]))

#dùng unpaking để lấy các giá trị mảng như Rest trong javascript
lit = [0,2,3]
idx0, *u = lit
print(idx0)  #lấy giá trị đầu
print(u)    #list các giá trị còn lại

####_______Django________###
#django là mô hình mvc trong đó view đóng vai trò là controller, templates đóng vai trò là view. 
  #nên còn được gọi là mô hình mvt
  
####______Phần View______#
 #1. Tải Django: pip install django
 #2. Tạo project: django-admin startproject projectname
 #3. Tạo app: django-admin startapp appname
     #tạo app phải khai báo tên app ở chỗ "INSTALLED_APPS" trong files settings.py
 #4. Chạy: python manage.py runserver

 #trong app mới tạo thư mục 'templates'
   #có base.html : là bộ khung web
   #và các page .html khác
   #dùng các khối để linh hoạt nội dung trong các trang cùng vị trí {% block nameblock %} {% endblock %}
 #trong app này còn tạo thư mục static chứa file css/js/img...
   #để dùng static cần load để trong phần head của base.html: {% load static %}
   #để gọi các file trong static: {% static 'đường dẫn' %}
 
 #vào file urls.py trong app chính (cùng tên project) cấu hình urls để thêm 1 path mới khi thêm app mới
 #trong app mới tạo thêm file urls.py để tạo ra các đường dẫn con với list: urlpatterns = []
   #nghĩa là app chính '/' rồi tới app con lại '/', ví dụ ở app chính là home, app phụ là contact thì: home/contact
 #file views.py trong app mới sẽ viết code chạy đến các templates trên 

 #Tóm lại, luồng xử lý là:
  #viết code trong 1 app thì: urls.py  >>  views.py  >>  html trong templates
  #file views.py sẽ gọi file html trong templates
      #file html trong templates của các app thông nhau, nên extend hay block app khác cũng được
      #từ views.py truyền dữ liệu vào html qua kiểu Dict và bên file html phải dùng Key của Dict để lấy dữ liệu
      #và views.py nhận dữ liệu từ file models.py
  #file urls.py trong app thì gọi lại view để hiển thị
      #file urls.py trong app chính lại gọi urls.py app phụ

  #khi gọi file models.py trong views.py cùng cấp thì import kiểu này: 
     #ngắn gọn: from .models import Post
     #hoặc: from . import models 
         #khi dùng thì lại phải thêm models.Post


###_______Phần Modal_____#
  #tạo db bằng ngôn ngữ python ko cần tới mysql

  #vào app file models tạo 1 class kế thừa 
  #thêm các trường
    #sau đó gõ lệnh: python manage.py makemigrations appname để tạo 1 model với trường id tự thêm
      #Mỗi lần thêm các trường mới thì cần : python manage.py makemigrations để cập nhật lại và python manage.py migrate để cập nhật bên server lưu
    #rồi gõ lệnh: python manage.py migrate để cập nhật dữ liệu vào sqlit
  #xem db sqlite bằng phần mềm db browser >> rồi mở tới tệp sqlite

###____Về Phần Admin__###
  #Django rất mạnh phần này, giúp quản lý csdl, có thể tạo filter, search, hiển thị các cột rất hay
    #đăng nhập tại: https://localhost:8000/admin
    #tạo user bằng: python manage.py createsuperuser
      #cái user này sẽ tạo trên terminal và dùng cho tất cả các app
      #trên giao diện trang admin sẽ có tất cả các app và model dữ liệu của từng app
    #vào file admin.py trong 1 app nào đó để xử lý code

###___Những cái khác cần chú ý____###
#khi truyền id thì phần urls.py phần path là <int:id> . trong đó int là kiểu của id
  #bên file views.py ngoài request thêm tham số id
#khi chỉnh sửa ở trang admin mà phần chuỗi có html hay xuống dòng để web hiển thị thì ở trang html cần như này
  #{{post.body | safe | linebreaks}} : trong đó safe để nhận biết html. linebreaks nhận biết xuống dòng

#test.py để viết các testcase
  #chạy test của 1 app thì lệnh: python manage.py test appname
    #nó sẽ chạy và hiển thị ở terminal
  #viêt class testcase đơn giản giọi request thì class đó kế thừa SimpleTestCase
   #nếu có liên quan đến modal thì class đó kế thừa TestCase
   #trong class testcase có hàm setUp(self) sẽ chạy đầu tiên

#ko code cưng url bằng cách thêm giá trị name
  #ví dụ url từ app chính đến app khác mà " " thì cũng đặt tên, gọi thì {% url 'namevuadat' %}
  #trường hợp <int:id> thì khi gọi {% url 'namevuadat' caigido.id %}
    #có lẽ lúc này Django sẽ tự biết được /id từ đâu để thêm vào url thành hoàn chỉnh

#Về Gereric giúp đỡ viết code ở file views.py nó giúp gọi bài viết, phân trang, đetail luôn
   #gọi đường dẫn hiện tại thì dùng : {{request.path}}

#Lỗi 404
  #trong setting.py để DEBUG=False, Host = ["*"] là chấp nhận tất cả
  #tạo file .html để tùy chỉnh giao diện lỗi
  #trong urls.py tổng: from django.conf.urls import handler404 
     #và gọi tơi views lỗi: handler404 = "home.views.error_404"
  #trong views.py lỗi thì thêm tham số thứ 2: exception

##-------Về xử lý image----####
#để đưa image về thư mục gốc, sẽ ko cần nếu như deploy lên server khác
  #Cài trong file settings.py app tổng, cái os cần import vào và phải cài thêm Pillow: python -m pip install Pillow
     #MEDIA_URL = "/media/"
     #MEDIA_ROOT = os.path.join(BASE_DIR, "media")
  #Cài trong file urls.py tổng cái này: 
     # import cái này
           # from django.conf.urls.static import static
           # from django.conf import settings
     
     # Thêm đoạn code này:
     #  if settings.DEBUG:
     #    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

     
##________Tạo user____-####
#cái này là tạo user quản lý trên trang admin có hể phân quyền
#form và xử lý form thì django hỗ trợ luôn hoặc tự chỉnh theo ý mình và có thể chỉnh css
    #xem lại code để biết cách code
#login/logout thì sẽ cũng có sẵn luôn
  #chú ý: file html login phải có dạng này: templates/registration/login.html
     #logout thì thêm trang sẽ chuyển tới trong file settings.py

###____deploy lên PythonAnyWhere_____##
#đăng ký tài khoản trên PythonAnyWhere.com, xong vào mục console để gõ lệnh, mục file để xem source code, web để dán các link tới file
#tạo môi trường ảo
    #lệnh: mkvirtualenv ten_myenv
       #lệnh tạo với phiên bản tùy chỉnh: mkvirtualenv --python=/usr/bin/python3.7 ten_myenv
        #để tạo môi trường ảo với câu lệnh trên trong file .bashrc phải thêm các dòng lệnh này
        # export WORKON_HOME=$HOME/.virtualenvs
        # export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.10  # Thay đổi đường dẫn đến Python cụ thể mà bạn muốn sử dụng
        # export VIRTUALENVWRAPPER_VIRTUALENV=/home/vuxuanbac/.local/bin/virtualenv  # Thay đổi thành đường dẫn của virtualenv đã xác định ở bước 2
        # source /usr/local/bin/virtualenvwrapper.sh
    #kích hoạt môi trường ảo: workon ten_myenv
#từ môi trường ảo clone code lên môi trường ảo
#cài các thư viện đã cài ở file requirements.txt: pip install -r requirements.txt
#chuyển các file static về 1 mối: python manage.py collectstatic
    #trong file settings.py phải có dòng lệnh này mới được: STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#cập nhật lại db: python manage.py migrate
#chú ý: ở mục WEB chỗ "WSGI configuration file:" nhấn vào vào điền đúng đường dẫn đến file chưa manage.py và file chứa settings.py. kiểu đường dẫn nối tiếp nhau luôn

#khi ta viết code thay đổi cần lên môi trường ảo pull lại code tự github về
    # git stash
    # git pull origin master
    # git stash apply
    #cập nhật lại static: python manage.py collectstatic --noinput

#Lỗi khi trên local thay đổi dữ liệu database khi đó dù up lên github nhưng khi vào pythonanywhere sẽ pull code rất khó khăn
   #Cách hay là xóa môi trường ảo và thư mục djangp clone từ git đi và tạo mới lại từ đầu
#Lỗi khi thêm các thư viện mà ko cập nhật lại vào file requirements.txt
#Lỗi phải chạy django trên môi trường ảo mới thực thi file wgsi

#Chú ý để Link CSS hoạt động thì thêm ?v=2 để xóa cache lưu đi : <link rel="stylesheet" href="{% static 'css/style.css' %}?v=2" type="text/css" />
