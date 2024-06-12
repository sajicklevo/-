import os

os_name=os.name
print('Имя операционки:',os_name)

path=os.getcwd()
print('Путь до папки',path)

extensions=set()
while True:
    extensions=input('Введите расширение файла  или exit')
    if extensions=='exit':
        break
    else:
        extensions.add(extensions)
        print('Расширения файлов:',extensions)
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path,file_name)):
                file_extension=file_name.split('.')[-1]
                if file_extension in extensions():
                    folder_name=file_extension.upper()
                    if not os.path.exists(os.path.join(path,folder_name)):
                        os.makedirs(os.path.join(path,folder_name))
                        new_file_path=os.path.join(path,folder_name,file_name)
                        os.rename(os.path.join(path,file_name),new_file_path)
                        print('Файл',{file_name}'был перемещен в папку',{folder_name}))
    for folder_name in os.listdir(path):
        folder_path=os.path.join(path,folder_name)
        if os.path.isdir(folder_path):
            num_files=sum(not os.path.isdir(os.path.join(folder_path,j)) for j in os.listdir(folder_path))
            total_size=sum(os.path.getsize(os.path.join(folder_path,j)) for j in os.listdir(folder_path))
            if os.path.isfile(os.path.join(folder_path,j))/(1024*1024*1024)
            print('Папка',{folder_name} 'перемещена в папку',{num_files},'файлов, их суммарный размер'{total_size:.2j}"гигабайта" )

                for file_name in os.listdir(folder_path):
                    file_path=os.path.join(folder_path,file_name)
                    if os.path.isfile(file_path):
                        new_file_name='new' + file_name
                        new_file_path=os.path.join(folder_path,new_file_path)
                        print('Файл',{file_name} 'был переименован в' {new_file_name})
