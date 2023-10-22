import streamlit as st


def space(n):
    for _ in range(n):
        st.write("")


def one_chart(dimensions, path_to_html, path_to_images,
              titles, descriptions, i, number_of_charts):

    # Dimensions
    col1, col2 = st.columns(2)
    with col1:
        dim1 = st.number_input("Width", min_value=1, max_value=12, value=6, step=1, key=i)
    with col2:
        dim2 = st.number_input("Height", min_value=1, max_value=12, value=6, step=1, key=i + number_of_charts)
    dimensions.append((dim1, dim2))
    st.write((dim1, dim2))

    # Path to HTML
    path_html = st.text_input("Path to HTML", key=i + 2 * number_of_charts)
    st.write(path_html)
    path_to_html.append(path_html)

    # Path to images
    path_image = st.text_input("Path to image", key=i + 3 * number_of_charts)
    st.write(path_image)
    path_to_images.append(path_image)

    # Title
    title = st.text_input("Title", key=i + 4 * number_of_charts)
    st.write(title)
    titles.append(title)

    # Description
    description = st.text_input("Description", key=i + 5 * number_of_charts)
    st.write(description)
    descriptions.append(description)

    return dimensions, path_to_html, path_to_images, titles, descriptions


def html_minify(dimensions: list,
                path_to_html: list,
                path_to_images: list,
                titles: list,
                descriptions: list) -> str:

    initial_text = "<section class=bg id=portfolio style=padding-top:10px><div class=container><div class=row id=portfolio-items>"
    final_text = "</div></div></section>"

    # Add all charts
    for i in range(len(dimensions)):
        dim1, dim2 = dimensions[i]
        path_html = path_to_html[i]
        path_image = path_to_images[i]
        title = titles[i]
        description = descriptions[i]

        # Add chart
        chart = f"<div class='portfolio-item col-sm-{dim1} col-md-{dim2}'><a class=portfolio-link href={path_html}><div class=portfolio-hover><div class=portfolio-hover-content><p>{title}<hr><p class=explanation_portfolio>{description}</div></div><img alt='{title}'class='img-fluid imgOfPortfolio'src={path_image}></a></div>"
        initial_text += chart

    # Add final text
    initial_text += final_text

    return initial_text

