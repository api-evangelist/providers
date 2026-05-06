---
aid: streamlit
name: Streamlit
description: Streamlit is an open-source Python framework that makes it easy to build and share beautiful, custom web apps for machine learning and data science. With Streamlit, you can turn data scripts into shareable web applications in minutes without needing front-end experience. Streamlit Community Cloud provides free hosting for Streamlit apps directly from GitHub repositories. The framework offers a Python API for displaying data, creating interactive widgets, caching computation, and connecting to databases and APIs.
url: https://raw.githubusercontent.com/api-evangelist/streamlit/refs/heads/main/apis.yml
image: https://streamlit.io/images/brand/streamlit-mark-color.png
tags:
  - Data Science
  - Machine Learning
  - Open Source
  - Python
  - Web Applications
type: Index
access: 3rd-Party
position: Consumer
created: '2025-02-12'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: streamlit:streamlit-python-api
    name: Streamlit Python API
    description: 'The Streamlit Python library API provides a rich set of functions for building interactive data applications. Organized by activity type: display data (st.write, st.dataframe, st.table), input widgets (st.button, st.slider, st.selectbox), layout (st.columns, st.tabs, st.sidebar), media (st.image, st.video, st.audio), charts (st.line_chart, st.bar_chart, st.map), and performance (st.cache_data, st.cache_resource). Also includes connection management via st.connection.'
    humanURL: https://docs.streamlit.io/develop/api-reference
    tags:
      - Data Science
      - Machine Learning
      - Open Source
      - Python
      - Web Applications
    properties:
      - type: Documentation
        url: https://docs.streamlit.io/develop/api-reference
      - type: GitHub
        url: https://github.com/streamlit/streamlit
      - type: Changelog
        url: https://docs.streamlit.io/develop/quick-reference/changelog
  - aid: streamlit:streamlit-cloud-api
    name: Streamlit Community Cloud API
    description: The Streamlit Community Cloud API provides programmatic access to manage deployed Streamlit applications. Supports deploying apps from GitHub repositories, managing app secrets, restarting apps, and workspace management. Authentication uses bearer tokens issued from account settings.
    humanURL: https://docs.streamlit.io/deploy/streamlit-community-cloud
    baseURL: https://api.streamlit.io/v1
    tags:
      - Cloud
      - Deployment
      - DevOps
      - Open Source
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/streamlit/refs/heads/main/openapi/streamlit-cloud-openapi.yml
      - type: Documentation
        url: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app
common:
  - type: Website
    url: https://streamlit.io
  - type: Documentation
    url: https://docs.streamlit.io
  - type: GitHub
    url: https://github.com/streamlit/streamlit
  - type: Forum
    url: https://discuss.streamlit.io
  - type: Blog
    url: https://blog.streamlit.io
  - type: Gallery
    url: https://streamlit.io/gallery
  - type: Changelog
    url: https://docs.streamlit.io/develop/quick-reference/changelog
  - type: Terms of Service
    url: https://streamlit.io/terms-of-use
  - type: Privacy Policy
    url: https://streamlit.io/privacy-policy
  - type: Sign Up
    url: https://share.streamlit.io/signup
  - type: PyPI
    url: https://pypi.org/project/streamlit/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/streamlit/refs/heads/main/openapi/streamlit-cloud-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/streamlit/refs/heads/main/json-schema/streamlit-app-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/streamlit/refs/heads/main/json-ld/streamlit-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
