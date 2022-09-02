# Generated by Django 3.0.10 on 2020-09-18 15:04

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200918_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content',
            field=wagtail.core.fields.StreamField([('big_text_section_block', wagtail.core.blocks.StructBlock([('text_block_top', wagtail.core.blocks.TextBlock(help_text='Use "<count" to insert stores quantity automatically. Ex. "We have <count> stores" --> "We have 22 stores"', required=False)), ('text_block_top_subtext', wagtail.core.blocks.TextBlock(max_length=999, required=False))])), ('category_carousel', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('category_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('page_link', wagtail.core.blocks.CharBlock(help_text='Use <location_slug> to insert location slug', required=False)), ('button_text', wagtail.core.blocks.CharBlock(max_length=255, required=False))])))])), ('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='To highlight the word into red please put it inside these tags: <b>…text…</b>', required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=55, required=True)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('social_icons_banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Join The TrailersPlus Community', required=False)), ('text', wagtail.core.blocks.CharBlock(default='Stay Up to Date With the Latest and Greatest', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('partners', streams.blocks.PartnersBlock()), ('big_banner', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional', max_length=1000, required=False)), ('buttons', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('button_icon', wagtail.images.blocks.ImageChooserBlock(help_text='Icon for Button(Optional)', required=False)), ('button_title', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('button_link', wagtail.core.blocks.CharBlock(max_length=999, required=False)), ('open_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False))])))])), ('banners_block', wagtail.core.blocks.StructBlock([('title_left_banner', wagtail.core.blocks.CharBlock(required=False)), ('sub_title_left_banner', wagtail.core.blocks.CharBlock(required=False)), ('image_left_banner', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt_left', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('left_banner_link_url', wagtail.core.blocks.CharBlock(blank=True, max_length=500)), ('title_right_banner', wagtail.core.blocks.CharBlock(required=False)), ('sub_title_right_banner', wagtail.core.blocks.CharBlock(required=False)), ('image_right_banner', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt_right', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('right_banner_link_url', wagtail.core.blocks.CharBlock(blank=True, max_length=500))])), ('recent_works', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=True, max_length=250)), ('background_color_grey', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('works', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_title', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('link', wagtail.core.blocks.CharBlock(max_length=255, required=False))])))])), ('richtext_block', streams.blocks.RichtextBlock()), ('single_image_block', wagtail.core.blocks.StructBlock([('single_image', wagtail.images.blocks.ImageChooserBlock()), ('single_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('share_btn', streams.blocks.ShareBtn()), ('call_us_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('sub_text', wagtail.core.blocks.TextBlock(help_text='For example: Please call us at <b><a href="tel:+1877-850-7587">877-850-7587</a></b> to discuss!', required=False))])), ('youtube_block', streams.blocks.YoutubeEmbedBlock()), ('next_previous_posts_block', streams.blocks.NextPreviousPostsS()), ('next_previous_posts_block1', wagtail.core.blocks.StructBlock([('next_text_button', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('previous_text_button', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('divider_line', streams.blocks.DividerLine())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content_en',
            field=wagtail.core.fields.StreamField([('big_text_section_block', wagtail.core.blocks.StructBlock([('text_block_top', wagtail.core.blocks.TextBlock(help_text='Use "<count" to insert stores quantity automatically. Ex. "We have <count> stores" --> "We have 22 stores"', required=False)), ('text_block_top_subtext', wagtail.core.blocks.TextBlock(max_length=999, required=False))])), ('category_carousel', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('category_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('page_link', wagtail.core.blocks.CharBlock(help_text='Use <location_slug> to insert location slug', required=False)), ('button_text', wagtail.core.blocks.CharBlock(max_length=255, required=False))])))])), ('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='To highlight the word into red please put it inside these tags: <b>…text…</b>', required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=55, required=True)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('social_icons_banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Join The TrailersPlus Community', required=False)), ('text', wagtail.core.blocks.CharBlock(default='Stay Up to Date With the Latest and Greatest', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('partners', streams.blocks.PartnersBlock()), ('big_banner', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional', max_length=1000, required=False)), ('buttons', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('button_icon', wagtail.images.blocks.ImageChooserBlock(help_text='Icon for Button(Optional)', required=False)), ('button_title', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('button_link', wagtail.core.blocks.CharBlock(max_length=999, required=False)), ('open_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False))])))])), ('banners_block', wagtail.core.blocks.StructBlock([('title_left_banner', wagtail.core.blocks.CharBlock(required=False)), ('sub_title_left_banner', wagtail.core.blocks.CharBlock(required=False)), ('image_left_banner', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt_left', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('left_banner_link_url', wagtail.core.blocks.CharBlock(blank=True, max_length=500)), ('title_right_banner', wagtail.core.blocks.CharBlock(required=False)), ('sub_title_right_banner', wagtail.core.blocks.CharBlock(required=False)), ('image_right_banner', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt_right', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('right_banner_link_url', wagtail.core.blocks.CharBlock(blank=True, max_length=500))])), ('recent_works', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=True, max_length=250)), ('background_color_grey', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('works', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_title', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('link', wagtail.core.blocks.CharBlock(max_length=255, required=False))])))])), ('richtext_block', streams.blocks.RichtextBlock()), ('single_image_block', wagtail.core.blocks.StructBlock([('single_image', wagtail.images.blocks.ImageChooserBlock()), ('single_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('share_btn', streams.blocks.ShareBtn()), ('call_us_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('sub_text', wagtail.core.blocks.TextBlock(help_text='For example: Please call us at <b><a href="tel:+1877-850-7587">877-850-7587</a></b> to discuss!', required=False))])), ('youtube_block', streams.blocks.YoutubeEmbedBlock()), ('next_previous_posts_block', streams.blocks.NextPreviousPostsS()), ('next_previous_posts_block1', wagtail.core.blocks.StructBlock([('next_text_button', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('previous_text_button', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('divider_line', streams.blocks.DividerLine())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content_es',
            field=wagtail.core.fields.StreamField([('big_text_section_block', wagtail.core.blocks.StructBlock([('text_block_top', wagtail.core.blocks.TextBlock(help_text='Use "<count" to insert stores quantity automatically. Ex. "We have <count> stores" --> "We have 22 stores"', required=False)), ('text_block_top_subtext', wagtail.core.blocks.TextBlock(max_length=999, required=False))])), ('category_carousel', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('category_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('page_link', wagtail.core.blocks.CharBlock(help_text='Use <location_slug> to insert location slug', required=False)), ('button_text', wagtail.core.blocks.CharBlock(max_length=255, required=False))])))])), ('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='To highlight the word into red please put it inside these tags: <b>…text…</b>', required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=55, required=True)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('social_icons_banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Join The TrailersPlus Community', required=False)), ('text', wagtail.core.blocks.CharBlock(default='Stay Up to Date With the Latest and Greatest', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('partners', streams.blocks.PartnersBlock()), ('big_banner', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional', max_length=1000, required=False)), ('buttons', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('button_icon', wagtail.images.blocks.ImageChooserBlock(help_text='Icon for Button(Optional)', required=False)), ('button_title', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('button_link', wagtail.core.blocks.CharBlock(max_length=999, required=False)), ('open_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False))])))])), ('banners_block', wagtail.core.blocks.StructBlock([('title_left_banner', wagtail.core.blocks.CharBlock(required=False)), ('sub_title_left_banner', wagtail.core.blocks.CharBlock(required=False)), ('image_left_banner', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt_left', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('left_banner_link_url', wagtail.core.blocks.CharBlock(blank=True, max_length=500)), ('title_right_banner', wagtail.core.blocks.CharBlock(required=False)), ('sub_title_right_banner', wagtail.core.blocks.CharBlock(required=False)), ('image_right_banner', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt_right', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('right_banner_link_url', wagtail.core.blocks.CharBlock(blank=True, max_length=500))])), ('recent_works', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=True, max_length=250)), ('background_color_grey', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('works', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_title', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('link', wagtail.core.blocks.CharBlock(max_length=255, required=False))])))])), ('richtext_block', streams.blocks.RichtextBlock()), ('single_image_block', wagtail.core.blocks.StructBlock([('single_image', wagtail.images.blocks.ImageChooserBlock()), ('single_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('share_btn', streams.blocks.ShareBtn()), ('call_us_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('sub_text', wagtail.core.blocks.TextBlock(help_text='For example: Please call us at <b><a href="tel:+1877-850-7587">877-850-7587</a></b> to discuss!', required=False))])), ('youtube_block', streams.blocks.YoutubeEmbedBlock()), ('next_previous_posts_block', streams.blocks.NextPreviousPostsS()), ('next_previous_posts_block1', wagtail.core.blocks.StructBlock([('next_text_button', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('previous_text_button', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('divider_line', streams.blocks.DividerLine())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bloglistingpage',
            name='content',
            field=wagtail.core.fields.StreamField([('slider_block', wagtail.core.blocks.StructBlock([('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='To highlight the word into red please put it inside these tags: <b>…text…</b>', max_length=999, required=False))])))])), ('big_text_section_block', wagtail.core.blocks.StructBlock([('text_block_top', wagtail.core.blocks.TextBlock(help_text='Use "<count" to insert stores quantity automatically. Ex. "We have <count> stores" --> "We have 22 stores"', required=False)), ('text_block_top_subtext', wagtail.core.blocks.TextBlock(max_length=999, required=False))])), ('category_carousel', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('category_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('page_link', wagtail.core.blocks.CharBlock(help_text='Use <location_slug> to insert location slug', required=False)), ('button_text', wagtail.core.blocks.CharBlock(max_length=255, required=False))])))])), ('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='To highlight the word into red please put it inside these tags: <b>…text…</b>', required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=55, required=True)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('social_icons_banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Join The TrailersPlus Community', required=False)), ('text', wagtail.core.blocks.CharBlock(default='Stay Up to Date With the Latest and Greatest', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('partners', streams.blocks.PartnersBlock()), ('big_banner', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional', max_length=1000, required=False)), ('buttons', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('button_icon', wagtail.images.blocks.ImageChooserBlock(help_text='Icon for Button(Optional)', required=False)), ('button_title', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('button_link', wagtail.core.blocks.CharBlock(max_length=999, required=False)), ('open_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False))])))])), ('banners_block', wagtail.core.blocks.StructBlock([('title_left_banner', wagtail.core.blocks.CharBlock(required=False)), ('sub_title_left_banner', wagtail.core.blocks.CharBlock(required=False)), ('image_left_banner', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt_left', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('left_banner_link_url', wagtail.core.blocks.CharBlock(blank=True, max_length=500)), ('title_right_banner', wagtail.core.blocks.CharBlock(required=False)), ('sub_title_right_banner', wagtail.core.blocks.CharBlock(required=False)), ('image_right_banner', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt_right', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('right_banner_link_url', wagtail.core.blocks.CharBlock(blank=True, max_length=500))])), ('recent_works', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=True, max_length=250)), ('background_color_grey', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('works', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_title', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('link', wagtail.core.blocks.CharBlock(max_length=255, required=False))])))])), ('carousel_popup', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('parts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('popup_id', wagtail.core.blocks.IntegerBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=200)), ('description', wagtail.core.blocks.TextBlock(max_length=1000, required=False)), ('price', wagtail.core.blocks.TextBlock(required=False)), ('main_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('gallery_images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))), ('options', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('option', wagtail.core.blocks.RichTextBlock(required=False))])))])))])), ('richtext_block', streams.blocks.RichtextBlock()), ('single_image_block', wagtail.core.blocks.StructBlock([('single_image', wagtail.images.blocks.ImageChooserBlock()), ('single_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('share_btn', streams.blocks.ShareBtn()), ('call_us_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('sub_text', wagtail.core.blocks.TextBlock(help_text='For example: Please call us at <b><a href="tel:+1877-850-7587">877-850-7587</a></b> to discuss!', required=False))])), ('youtube_block', streams.blocks.YoutubeEmbedBlock()), ('divider_line', streams.blocks.DividerLine())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bloglistingpage',
            name='content_en',
            field=wagtail.core.fields.StreamField([('slider_block', wagtail.core.blocks.StructBlock([('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='To highlight the word into red please put it inside these tags: <b>…text…</b>', max_length=999, required=False))])))])), ('big_text_section_block', wagtail.core.blocks.StructBlock([('text_block_top', wagtail.core.blocks.TextBlock(help_text='Use "<count" to insert stores quantity automatically. Ex. "We have <count> stores" --> "We have 22 stores"', required=False)), ('text_block_top_subtext', wagtail.core.blocks.TextBlock(max_length=999, required=False))])), ('category_carousel', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('category_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('page_link', wagtail.core.blocks.CharBlock(help_text='Use <location_slug> to insert location slug', required=False)), ('button_text', wagtail.core.blocks.CharBlock(max_length=255, required=False))])))])), ('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='To highlight the word into red please put it inside these tags: <b>…text…</b>', required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=55, required=True)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('social_icons_banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Join The TrailersPlus Community', required=False)), ('text', wagtail.core.blocks.CharBlock(default='Stay Up to Date With the Latest and Greatest', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('partners', streams.blocks.PartnersBlock()), ('big_banner', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional', max_length=1000, required=False)), ('buttons', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('button_icon', wagtail.images.blocks.ImageChooserBlock(help_text='Icon for Button(Optional)', required=False)), ('button_title', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('button_link', wagtail.core.blocks.CharBlock(max_length=999, required=False)), ('open_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False))])))])), ('banners_block', wagtail.core.blocks.StructBlock([('title_left_banner', wagtail.core.blocks.CharBlock(required=False)), ('sub_title_left_banner', wagtail.core.blocks.CharBlock(required=False)), ('image_left_banner', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt_left', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('left_banner_link_url', wagtail.core.blocks.CharBlock(blank=True, max_length=500)), ('title_right_banner', wagtail.core.blocks.CharBlock(required=False)), ('sub_title_right_banner', wagtail.core.blocks.CharBlock(required=False)), ('image_right_banner', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt_right', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('right_banner_link_url', wagtail.core.blocks.CharBlock(blank=True, max_length=500))])), ('recent_works', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=True, max_length=250)), ('background_color_grey', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('works', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_title', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('link', wagtail.core.blocks.CharBlock(max_length=255, required=False))])))])), ('carousel_popup', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('parts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('popup_id', wagtail.core.blocks.IntegerBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=200)), ('description', wagtail.core.blocks.TextBlock(max_length=1000, required=False)), ('price', wagtail.core.blocks.TextBlock(required=False)), ('main_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('gallery_images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))), ('options', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('option', wagtail.core.blocks.RichTextBlock(required=False))])))])))])), ('richtext_block', streams.blocks.RichtextBlock()), ('single_image_block', wagtail.core.blocks.StructBlock([('single_image', wagtail.images.blocks.ImageChooserBlock()), ('single_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('share_btn', streams.blocks.ShareBtn()), ('call_us_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('sub_text', wagtail.core.blocks.TextBlock(help_text='For example: Please call us at <b><a href="tel:+1877-850-7587">877-850-7587</a></b> to discuss!', required=False))])), ('youtube_block', streams.blocks.YoutubeEmbedBlock()), ('divider_line', streams.blocks.DividerLine())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bloglistingpage',
            name='content_es',
            field=wagtail.core.fields.StreamField([('slider_block', wagtail.core.blocks.StructBlock([('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='To highlight the word into red please put it inside these tags: <b>…text…</b>', max_length=999, required=False))])))])), ('big_text_section_block', wagtail.core.blocks.StructBlock([('text_block_top', wagtail.core.blocks.TextBlock(help_text='Use "<count" to insert stores quantity automatically. Ex. "We have <count> stores" --> "We have 22 stores"', required=False)), ('text_block_top_subtext', wagtail.core.blocks.TextBlock(max_length=999, required=False))])), ('category_carousel', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('category_title', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('page_link', wagtail.core.blocks.CharBlock(help_text='Use <location_slug> to insert location slug', required=False)), ('button_text', wagtail.core.blocks.CharBlock(max_length=255, required=False))])))])), ('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='To highlight the word into red please put it inside these tags: <b>…text…</b>', required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=55, required=True)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('social_icons_banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Join The TrailersPlus Community', required=False)), ('text', wagtail.core.blocks.CharBlock(default='Stay Up to Date With the Latest and Greatest', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('partners', streams.blocks.PartnersBlock()), ('big_banner', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock()), ('background_image_mobile', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional', max_length=1000, required=False)), ('buttons', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('button_icon', wagtail.images.blocks.ImageChooserBlock(help_text='Icon for Button(Optional)', required=False)), ('button_title', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('button_link', wagtail.core.blocks.CharBlock(max_length=999, required=False)), ('open_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False))])))])), ('banners_block', wagtail.core.blocks.StructBlock([('title_left_banner', wagtail.core.blocks.CharBlock(required=False)), ('sub_title_left_banner', wagtail.core.blocks.CharBlock(required=False)), ('image_left_banner', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt_left', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('left_banner_link_url', wagtail.core.blocks.CharBlock(blank=True, max_length=500)), ('title_right_banner', wagtail.core.blocks.CharBlock(required=False)), ('sub_title_right_banner', wagtail.core.blocks.CharBlock(required=False)), ('image_right_banner', wagtail.images.blocks.ImageChooserBlock()), ('background_image_alt_right', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('right_banner_link_url', wagtail.core.blocks.CharBlock(blank=True, max_length=500))])), ('recent_works', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=True, max_length=250)), ('background_color_grey', wagtail.core.blocks.BooleanBlock(default=False, required=False)), ('works', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_title', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('link', wagtail.core.blocks.CharBlock(max_length=255, required=False))])))])), ('carousel_popup', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('parts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('popup_id', wagtail.core.blocks.IntegerBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=200)), ('description', wagtail.core.blocks.TextBlock(max_length=1000, required=False)), ('price', wagtail.core.blocks.TextBlock(required=False)), ('main_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('gallery_images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))), ('options', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('option', wagtail.core.blocks.RichTextBlock(required=False))])))])))])), ('richtext_block', streams.blocks.RichtextBlock()), ('single_image_block', wagtail.core.blocks.StructBlock([('single_image', wagtail.images.blocks.ImageChooserBlock()), ('single_image_alt', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('share_btn', streams.blocks.ShareBtn()), ('call_us_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('sub_text', wagtail.core.blocks.TextBlock(help_text='For example: Please call us at <b><a href="tel:+1877-850-7587">877-850-7587</a></b> to discuss!', required=False))])), ('youtube_block', streams.blocks.YoutubeEmbedBlock()), ('divider_line', streams.blocks.DividerLine())], blank=True, null=True),
        ),
    ]
