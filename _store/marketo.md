---
aid: marketo
name: Marketo
description: Marketo, an Adobe company, develops and sells marketing automation software for account-based marketing and other marketing services and products, including SEO and content creation. Marketo Engage exposes a REST API for programmatic access to leads, programs, campaigns, assets, lists, and bulk import/export.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/marketo/refs/heads/main/apis.yml
tags:
  - Adobe
  - Automation
  - Marketing
  - Marketing Automation
created: '2023-11-23'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: marketo:marketo-engage-rest-api
    name: Marketo Engage REST API
    description: Marketo exposes a REST API which allows for remote execution of many of the systems capabilities. From creating programs to bulk lead import, there are many options which allow fine-grained control of a Marketo instance.
    humanURL: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/rest-api
    tags:
      - Assets
      - Campaigns
      - Email
      - Forms
      - Landing Pages
      - Leads
      - Marketing Automation
      - Programs
      - REST
      - Smart Lists
    properties:
      - type: Documentation
        url: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/rest-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/marketo/refs/heads/main/openapi/marketo-engage-rest-api-openapi.yml
common:
  - type: Portal
    url: https://developers.marketo.com/
  - type: GettingStarted
    url: https://developers.marketo.com/getting-started/
  - type: Webhooks
    url: https://developers.marketo.com/webhooks/
  - type: Libraries
    url: https://github.com/Marketo/Community-Supported-Client-Libraries
  - type: Contact
    url: http://www.marketo.com/company/contact/
  - type: Blog
    url: https://developers.marketo.com/blog/
  - type: TermsOfService
    url: https://www.marketo.com/company/legal/
  - type: Privacy
    url: http://legal.marketo.com/privacy/
  - type: License
    url: https://developers.marketo.com/api-license/
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
---
