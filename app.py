from collections import OrderedDict

import streamlit as st


# TODO : change TITLE, TEAM_MEMBERS and PROMOTION values in config.py.
import config

# TODO : you can (and should) rename and add tabs in the ./tabs folder, and import them here.
import intro, dataset, visualisation, modelisation,conclusion,test



st.set_page_config(
    page_title=config.TITLE,
    page_icon="https://previews.123rf.com/images/ylivdesign/ylivdesign1503/ylivdesign150300203/37170913-bleu-ic%C3%B4ne-euro.jpg",
)

with open("style.css", "r") as f:
    style = f.read()

st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)


# TODO: add new and/or renamed tab in this ordered dict by
# passing the name in the sidebar as key and the imported tab
# as value as follow :
TABS = OrderedDict(
    [
        (intro.sidebar_name, intro),
        (dataset.sidebar_name, dataset),
        (visualisation.sidebar_name, visualisation),
        (modelisation.sidebar_name,modelisation),
        (test.sidebar_name,test),
        (conclusion.sidebar_name,conclusion)
    ]
)

def run():
    st.sidebar.title('Prédiction du succès d’une campagne de Marketing d’une banque')
    st.sidebar.image(
        "https://www.techfunnel.com/wp-content/uploads/2018/03/Digital-Marketing-Trends-in-Banking.jpg",
        width=200,
    )
    tab_name = st.sidebar.radio("", list(TABS.keys()), 0)
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"## {config.PROMOTION}")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Team members:")
    for member in config.TEAM_MEMBERS:
        st.sidebar.markdown(member.sidebar_markdown(), unsafe_allow_html=True)

    tab = TABS[tab_name]

    tab.run()


if __name__ == "__main__":
    run()
