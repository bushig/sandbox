import re

acronyms=["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]

def shortify(item):
    word_list=item.split('-')
    if len(item)>30:
        result=''
        for word in word_list:
            if word not in acronyms:
                result+=word[0].upper()
        return result
    else:
        result=[]
        for word in word_list:
            result.append(word.upper())
        return ' '.join(result)



def generate_bc(url, separator):
    br_list=[]
    all_list = re.split(r'(?<!/)/(?=\w+)', url)
    print(all_list[-1])
    all_list[-1] = re.match(r'(?<!www\.)([\w\-]+)\.?(?:#|\?|)', all_list[-1]).group(1)
    if all_list[-1]== 'index':
        all_list.pop()
    print('original: {} \ngot: {}'.format(url,all_list))
    for i in range(len(all_list)):
        item=all_list[i]
        if len(all_list)==1:
            return '<span class="active">HOME</span>'

        elif i==0:
            br_list.append('<a href="/">HOME</a>')
        elif i==len(all_list)-1:
            br_list.append('<span class="active">'+shortify(item)+'</span>')
        else:
            url='/'.join(all_list[1:i+1])
            print(url)
            br_list.append('<a href="/'+url+'/">'+shortify(item)+'</a>')

    breadcrumb=separator.join(br_list)
    return breadcrumb




print(generate_bc("linkedin.it/eurasian-with-of-pippi-biotechnology/most-viewed/most-viewed/test.php#team", " : "))