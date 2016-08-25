# -*_coding:utf8-*-
import handle_html_file as htmlf
import db.dbhelper as afh
import constants as cons


def do():
    list_src = htmlf.explain_html(htmlf.get_file_path())
    # htmlf.write_to_file(list_src)

    # helper = afh.RankUSHelper()
    app_info_helper = afh.AppInfoHelper()
    for i in range(len(list_src)):
        # write the dict to file
        list = list_src[i]
        for j in range(len(list)):
            s_dict = list[j]
            # helper.add_by(s_dict)
            add_to_appinfo(app_info_helper, s_dict)
            print('#' + str(i) + '-' + str(j))
            print(s_dict)

    return


def add_to_appinfo(helper, s_dict):
    helper.add_or_update(s_dict[cons.FIELD_PACKAGE], '', '', '', '', '', s_dict[cons.FIELD_OFFERED],
                         '')


do()
