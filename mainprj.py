# Main
import k_food as kf
import fast_food as ff
import bunsik as bs
import streamlit as st

def food_main():
    st.write("추천 맛집 종류를 선택하세요!")
    menu_number = st.radio("맛집 종류", ["한식","패스트푸드", "분식"], index=None)
    
    if menu_number == '한식':
        st.write("\"한식\"을 선택하셨네요!")
        st.image('k_food.jpg', width=300)
        if not kf.k_food():             # 예산에 맞는 메뉴가 없을 경우 앞 모듈의 False값을 받아
            st.write("다시 선택해 주세요")
        
    elif menu_number == '패스트푸드':
        st.write("\"패스트푸드\"를 선택하셨네요!")
        st.image('fastfood.jpg', width=300)
        if not ff.fast_food():
            st.write("다시 선택해 주세요")
        
    elif menu_number == '분식':
        st.write("\"분식\"을 선택하셨네요!")
        st.image('bunsik.jpg', width=300)
        if not bs.bunsik():
            st.write("다시 선택해 주세요")
       
    