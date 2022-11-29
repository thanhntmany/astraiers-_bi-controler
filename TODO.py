- Tạo chức năng build/test diện rộng trên toàn project


Thiết kế chức năng metadata về dependcy để quá trình builder, debug triển khai tối ưu hơn.

Ý tưởng 1:
Để 1 script build/relase được run thì phải có thay đổi trong những file depend của script đó.


Astraiers Build Instruction

Thêm chức năng init cho từng module:
    VD: Setup .ass folder, download dependces

Thêm các chức năng mass run:
    git pull đồng thời cho các module
    git push đồng thời cùng chung 1 commit + description cho các module

Edit tương tác dạng gui để dev tiện làm việc hơn




_bi.json:
Them action dựng sẵn cho vụ build file