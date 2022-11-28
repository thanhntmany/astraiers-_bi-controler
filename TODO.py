- Tạo chức năng build/test diện rộng trên toàn project


Thiết kế chức năng metadata về dependcy để quá trình builder, debug triển khai tối ưu hơn.

Ý tưởng 1:
Để 1 script build/relase được run thì phải có thay đổi trong những file depend của script đó.


Astraiers Build Instruction

Thêm chức năng init cho từng module:
    VD: Setup .ass folder, download dependces