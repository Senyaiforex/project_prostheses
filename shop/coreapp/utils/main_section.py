def main_section(position, text_data, button_data,
                 image_data, header_data, list_data, form_data):
    name_section = f'section{position}'
    h1 = next((elem['data'] for elem in header_data if elem['type'] == 'h1'), None)
    h2 = [elem['data'] for elem in header_data if elem['type'] == 'h2']
    text = {elem['tag_dev']: elem['data'] for elem in text_data}
    images = [{'position': elem['position'],
               'image_url': elem['data']} for elem in image_data]
    related_lists = {elem['tag_dev']: elem['fields'] for elem in list_data}
    data_dict = {
            name_section: {
            }
    }
    if h1:
        data_dict[name_section]['h1'] = h1
    if h2:
        data_dict[name_section]['h2'] = h2 if len(h2) > 1 else h2[0]
    if text:
        for key, value in text.items():
            data_dict[name_section][key] = value
    if related_lists:
        for key, value in related_lists.items():
            data_dict[name_section][key] = value
    if images:
        data_dict[name_section]['images' if len(images) > 1 else 'image'] = images if len(images) > 1 else images[0]
    if button_data:
        data_dict[name_section]['buttons' if len(button_data) > 1 else 'button'] = button_data if len(
                button_data) > 1 else button_data[0]
    if form_data:
        data_dict[name_section]['forms' if len(form_data) > 1 else 'form'] = form_data if len(form_data) > 1 else \
            form_data[0]
    return data_dict
