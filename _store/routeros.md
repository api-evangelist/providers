---
aid: routeros
url: https://raw.githubusercontent.com/api-search/routeros/refs/heads/main/apis.yml
apis:
  - aid: routeros:routeros
    name: RouterOS
    tags:
      - API
    humanURL: https://help.mikrotik.com/docs/spaces/ROS/pages/47579160/API
    properties:
      - url: https://help.mikrotik.com/docs/spaces/ROS/pages/47579160/API
        type: Documentation
    description: |-

      API service must be enabled before trying to establish the API connection.
      By default, API uses TCP:8728 and TCP:8729 (secure). API-SSL service is
      capable of working in two modes - with and without a certificate. In the
      case no certificate is used in /ip service settings then an anonymous
      Diffie-Hellman cipher has to be used to establish a ...
name: RouterOS
tags:
  - API
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-07T00:00:00.000Z'
modified: '2024-11-07T00:00:00.000Z'
position: Consumer
description: |-

  API service must be enabled before trying to establish the API connection. By
  default, API uses TCP:8728 and TCP:8729 (secure). API-SSL service is capable
  of working in two modes - with and without a certificate. In the case no
  certificate is used in /ip service settings then an anonymous Diffie-Hellman
  cipher has to be used to establish a ...
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---