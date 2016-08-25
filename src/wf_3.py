# -*_coding:utf8-*-
import handle_html_file as htmlf
import db.dbhelper as afh


def do():
    list_src = htmlf.explain_html(htmlf.get_file_path())

    helper = afh.RankUSHelper()
    for i in range(len(list_src)):
        # write the dict to file
        list = list_src[i]
        for s_dict in list:
            helper.and_or_update_by(s_dict)
            print('#', str(i))
            print(s_dict)

    return


do()
