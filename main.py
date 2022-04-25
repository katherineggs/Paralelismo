import pandas as pd
import multiprocessing as mp
import csv  
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

threads_num = 4

def todo(i):
    n = 1 + i
    n_str = str(n)
    file = 'index_data_' + n_str + '.csv'
    df = pd.read_csv(file)
    head = []
    for col in df.columns:
        head.append(col)
    head.remove('dates')


    
    avg1 = ['mean']
    std1= ['std']
    count1 = ['count']
    min1 =  ['min']
    max1 = ['max']
    for i in head:
        
        avg1.append(Average(i,df))
        std1.append(std(i,df))
        count1.append(count(i,df))
        min1.append(min(i,df))
        max1.append(max(i,df))
    data = [avg1,std1,count1,min1,max1]
  

    header = head
    header.insert(0,'type')
    f = 'archivo_out_' + n_str + '.csv'
    with open(f, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)



def Average(col,df):
    return df[col].mean()

def std (col,df):
    return df[col].std()

def count (col,df):
    return df[col].count()

def min (col,df):
    return df[col].min()

def max (col,df): 
    return df[col].max()





#-------------------------------------------forma secuencial-------------------------------------------------------------------------------------
# t1 = time.perf_counter()
# for i in range(999): 
#     todo(i)
# t2 = time.perf_counter()


# #----------------------------------------------------------------------------paralelizacion de funciones-------------------------------------------------------------


def count_para1(i):
    for i in range(999):
        n = 1 + i
        n_str = str(n)
        file = 'index_data_' + n_str + '.csv'
        df = pd.read_csv(file)
        head = []
        for col in df.columns:
            head.append(col)
        head.remove('dates')


        list1 = 'count,'
        
        for i in head:
            list1 = list1 + ','+ str(count(i,df))  + ','

        f = 'archivo_out_' + n_str + '.csv'
        with open(f, 'a+', encoding='UTF8', newline='') as f:
            f.write(list1)
           
def mean_para1(i):
    for i in range(999):
        n = 1 + i
        n_str = str(n)
        file = 'index_data_' + n_str + '.csv'
        df = pd.read_csv(file)
        head = []
        for col in df.columns:
            head.append(col)
        head.remove('dates')

       

        list1 = 'mean,'
        
        for i in head:
            list1 = list1 + ','+ str(Average(i,df))  + ","

        f = 'archivo_out_' + n_str + '.csv'
        with open(f, 'a+', encoding='UTF8', newline='') as f:
            f.write(list1)

def std_para1(i):
    for i in range(999):
        n = 1 + i
        n_str = str(n)
        file = 'index_data_' + n_str + '.csv'
        df = pd.read_csv(file)
        head = []
        for col in df.columns:
            head.append(col)
        head.remove('dates')

  

        list1 = 'std,'
    
        for i in head:
            list1 = list1 + ','+ str(std(i,df))  + ','

        f = 'archivo_out_' + n_str + '.csv'
        with open(f, 'a+', encoding='UTF8', newline='') as f:
            f.write(list1)

def min_para1(i):
    for i in range(999):
        n = 1 + i
        n_str = str(n)
        file = 'index_data_' + n_str + '.csv'
        df = pd.read_csv(file)
        head = []
        for col in df.columns:
            head.append(col)
        head.remove('dates')

      

        list1 = 'min,' 
    
        for i in head:
            list1 = list1 + ','+ str(min(i,df))  + ','

        f = 'archivo_out_' + n_str + '.csv'
        with open(f, 'a+', encoding='UTF8', newline='') as f:
            f.write(list1)

def max_para1(i):
    for i in range(999): 
        n = 1 + i
        n_str = str(n)
        file = 'index_data_' + n_str + '.csv'
        df = pd.read_csv(file)
        head = []
        for col in df.columns:
            head.append(col)
        head.remove('dates')

       

        list1 ='max,'
    
        for i in head:
            list1 = list1 + ','+ str(max(i,df)) + ','

        f = 'archivo_out_' + n_str + '.csv'
        with open(f, 'a+', encoding='UTF8', newline='') as f:
            f.write(list1)




# t7 = time.perf_counter()
# if __name__ == '__main__':
#     with ProcessPoolExecutor(max_workers=threads_num) as exe:
#             exe.submit(count_para1,threads_num)
#             exe.submit(mean_para1,threads_num)
#             exe.submit(std_para1,threads_num)
#             exe.submit(min_para1,threads_num)
#             exe.submit(max_para1,threads_num)
            


# t8 = time.perf_counter()
# #----------------------------------------------------------------------------paralelizacion de archivos--------------------------------------------------------------



# l = [i for i in range(999)]
# l.remove(0)
 
# t5 = time.perf_counter()
 

# if __name__ == '__main__':
#     result =[]
#     with ThreadPoolExecutor(max_workers= threads_num) as exe:
       
#         result = exe.map(todo,l)

# t6 = time.perf_counter()

#----------------------------------------------------------------------------paralelizacion de archivos y funciones--------------------------------------------------

#MULTITHREADING TASKS
def count_para(i):
    n = 1 + i
    n_str = str(n)
    file = 'index_data_' + n_str + '.csv'
    df = pd.read_csv(file)
    head = []
    for col in df.columns:
        head.append(col)
    head.remove('dates')

 
    list1 = 'count,'
    
    for i in head:
        list1 = list1 + ','+ str(count(i,df))  + ','

    f = 'archivo_out_' + n_str + '.csv'
    with open(f, 'a+', encoding='UTF8', newline='') as f:
        f.write(list1)

           
def mean_para(i):
    n = 1 + i
    n_str = str(n)
    file = 'index_data_' + n_str + '.csv'
    df = pd.read_csv(file)
    head = []
    for col in df.columns:
        head.append(col)
    head.remove('dates')

  

    list1 = 'mean,'
    
    for i in head:
        list1 = list1 + ','+ str(Average(i,df))  + ","

    f = 'archivo_out_' + n_str + '.csv'
    with open(f, 'a+', encoding='UTF8', newline='') as f:
        f.write(list1)

def std_para(i):
    n = 1 + i
    n_str = str(n)
    file = 'index_data_' + n_str + '.csv'
    df = pd.read_csv(file)
    head = []
    for col in df.columns:
        head.append(col)
    head.remove('dates')

   

    list1 = 'std,'
    
    for i in head:
        list1 = list1 + ','+ str(std(i,df))  + ','

    f = 'archivo_out_' + n_str + '.csv'
    with open(f, 'a+', encoding='UTF8', newline='') as f:
       f.write(list1)


def min_para(i):
    n = 1 + i
    n_str = str(n)
    file = 'index_data_' + n_str + '.csv'
    df = pd.read_csv(file)
    head = []
    for col in df.columns:
        head.append(col)
    head.remove('dates')

   

    list1 = 'min,'
    
    for i in head:
        list1 = list1 + ','+ str(min(i,df))  + ','

    f = 'archivo_out_' + n_str + '.csv'
    with open(f, 'a+', encoding='UTF8', newline='') as f:
        f.write(list1)


def max_para(i):
    n = 1 + i
    n_str = str(n)
    file = 'index_data_' + n_str + '.csv'
    df = pd.read_csv(file)
    head = []
    for col in df.columns:
        head.append(col)
    head.remove('dates')

    

    list1 ='max,'
    
    for i in head:
        list1 = list1 + ','+ str(max(i,df)) + ','

    f = 'archivo_out_' + n_str + '.csv'
    with open(f, 'a+', encoding='UTF8', newline='') as f:
        f.write(list1)




# l = [i for i in range(999)]
# l.remove(0)
# t3 = time.perf_counter()
# if __name__ == '__main__':
#     with ProcessPoolExecutor(max_workers=threads_num) as exe:
#             # Maps the method 'single file' with a list of path.
#             exe.submit(count_para,l)
#             exe.submit(mean_para,l)
#             exe.submit(std_para,l)
#             exe.submit(min_para,l)
#             exe.submit(max_para,l)
#             result = exe.map(count_para,l)
#             result = exe.map(mean_para,l)
#             result = exe.map(std_para,l)
#             result = exe.map(min_para,l)
#             result = exe.map(max_para,l)
            


# t4 = time.perf_counter()




#-------------------------------------------forma secuencial-------------------------------------------------------------------------------------
def secuencial():
    t1 = time.perf_counter()
    for i in range(999): 
        todo(i)
    t2 = time.perf_counter()
    return t1,t2

# #----------------------------------------------------------------------------paralelizacion de archivos--------------------------------------------------------------


def archivos(threads_num):
    l = [i for i in range(999)]
    l.remove(0)
    
    t5 = time.perf_counter()
    

    if __name__ == '__main__':
        result =[]
        with ThreadPoolExecutor(max_workers= threads_num) as exe:
        
            result = exe.map(todo,l)

    t6 = time.perf_counter()
    return t5,t6



#------------------------------------------------------------Paralelizacion por archivos y funciones-----------------------------------------------------------
def archivosYfunciones(threads_num):
    l = [i for i in range(999)]
    l.remove(0)
    t3 = time.perf_counter()
    if __name__ == '__main__':
        with ProcessPoolExecutor(max_workers=threads_num) as exe:
                # Maps the method 'single file' with a list of path.
                exe.submit(count_para,l)
                exe.submit(mean_para,l)
                exe.submit(std_para,l)
                exe.submit(min_para,l)
                exe.submit(max_para,l)
                result = exe.map(count_para,l)
                result = exe.map(mean_para,l)
                result = exe.map(std_para,l)
                result = exe.map(min_para,l)
                result = exe.map(max_para,l)
                


    t4 = time.perf_counter()
    return t3,t4

#------------------------------------------------Paralelizacion de Funciones
def funciones(threads_num):
    t7 = time.perf_counter()
    if __name__ == '__main__':
        with ProcessPoolExecutor(max_workers=threads_num) as exe:
                exe.submit(count_para1,threads_num)
                exe.submit(mean_para1,threads_num)
                exe.submit(std_para1,threads_num)
                exe.submit(min_para1,threads_num)
                exe.submit(max_para1,threads_num)
                


    t8 = time.perf_counter()
    return t7,t8



lista_threads = [1,2,4,8]
for n in lista_threads:
    for i in range(10):
        t5,t6= archivos(n)
        t7,t8= funciones(n)
        t3,t4=archivosYfunciones(n)
        t1,t2=secuencial()

        print(f'Codigo secuencial tomo:{t2 - t1} segundos con {n} threads')
        print(f'Codigo con funciones paralelizadas tomo :{t8 - t7} segundos con {n} threads')
        print(f'Codigo con archivos paralelizados tomo :{t6 - t5} segundos con {n} threads')
        print(f'Codigo con funciones paralelizadas y archivos paralelizados tomo :{t4 - t3} segundos con {n} threads')
