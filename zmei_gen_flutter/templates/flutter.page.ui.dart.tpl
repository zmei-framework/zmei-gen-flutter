import 'package:flutter/material.dart';
import '../../pages/{{ page.application.app_name }}/{{ page.name }}.dart';
import './../../app.dart';


{% if not page.uri %}abstract {% endif %}class {{ page.view_name }}StateUi extends {{ page.view_name }}State {
    {% if page.uri %}
    Widget buildBody(BuildContext context) {
        return this.buildContent(context);
    }
    {% endif %}
    {%- if page.auto_page %}
    @override
    Widget buildDrawer() {}
    {% endif %}
}