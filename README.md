Notes:

Using the streamlit library: https://docs.streamlit.io/

I had to use Git Large File Storage to host our data since its larger than 100 Mb: 
* https://discuss.streamlit.io/t/faq-how-to-use-large-files-in-your-streamlit-app/64621
* https://www.youtube.com/watch?v=jXsvFfksvd0

Update: This isn't necessary. Our file wasn't actually that big. There was some sort of error when turning it into a csv that made the file size balloon up.

Used streamlit-aggrid for the dataframe
* https://discuss.streamlit.io/t/multi-column-headers/37847/4
* https://www.youtube.com/watch?v=F54ELJwspos
* https://streamlit-aggrid.readthedocs.io/en/docs/GridOptionsBuilder.html
* https://freedium.cfd/https://towardsdatascience.com/7-reasons-why-you-should-use-the-streamlit-aggrid-component-2d9a2b6e32f0
