import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Tiêu đề cho ứng dụng
st.title('Ứng dụng Tính Toán Hấp Dẫn')

# Thêm một mô tả ngắn cho ứng dụng
st.markdown('Chào mừng bạn đến với ứng dụng tính toán của tôi! Chọn một giá trị và xem kết quả.')

# Slider để người dùng chọn giá trị
x = st.slider('Chọn một giá trị', 0, 100, 50)

# Tính toán bình phương và căn bậc 2
squared = x * x
sqrt = np.sqrt(x)

# Hiển thị kết quả
st.write(f'Giá trị bạn chọn là: {x}')
st.write(f'Bình phương của {x} là: {squared}')
st.write(f'Căn bậc 2 của {x} là: {sqrt:.2f}')

# Vẽ biểu đồ đồ thị của y = x^2
fig, ax = plt.subplots()
x_values = np.linspace(0, 100, 100)
y_values = x_values ** 2
ax.plot(x_values, y_values, label='y = x^2')
ax.scatter(x, squared, color='red', label=f'({x}, {squared})', zorder=5)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Đồ thị hàm y = x^2')

# Thêm chú thích cho biểu đồ
ax.legend()

# Hiển thị biểu đồ trong ứng dụng Streamlit
st.pyplot(fig)

# Thêm hình ảnh hoặc ảnh minh họa
st.image('https://scontent.fhan14-5.fna.fbcdn.net/v/t39.30808-6/480704546_656081827085500_6713358780786447948_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHjmnT_iJAoA2uDKAazqf_kEeGXDFDmOwwR4ZcMUOY7DPjQMbTsgUMH4eAaWxyfPBnmWM_9GhKxtImegTPVzklb&_nc_ohc=ZobGzWNTDw4Q7kNvgEs3Li_&_nc_oc=AdjHyrwPy-gzigZjPbirYAeGYKHZ4xe5V3WhXqv09luLr30bkPPvGg3ahsAIpNjjTdU&_nc_zt=23&_nc_ht=scontent.fhan14-5.fna&_nc_gid=A6PUG_SrGe9w8dxek5YraFA&oh=00_AYF6JMX5yZMoDk4SNVr6Kp9XKkg4iggT0hvIQjS3cHeTqA&oe=67D3BDED', caption='Test cho code moi', use_column_width=True)

# Thêm một widget nhập liệu khác (text input)
text_input = st.text_input('Nhập một câu trả lời thú vị', 'Hello World!')
st.write(f'Bạn đã nhập: {text_input}')
