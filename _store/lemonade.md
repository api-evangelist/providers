---
aid: lemonade
name: Lemonade
description: Lemonade, Inc. is an American insurance company. The company offers renters, homeowners, car, pet, and term life insurance in the United States, as well as contents and liability policies in Germany and the Netherlands and renters insurance in France. The Lemonade Insurance API allows partners to embed insurance quoting, policy creation, and payment flows for homeowners, condo, and renters policies into their own websites and apps.
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
tags:
  - Insurance
  - Renters Insurance
  - Homeowners Insurance
  - Embedded Insurance
url: https://raw.githubusercontent.com/api-evangelist/lemonade/refs/heads/main/apis.yml
created: '2024-07-02'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: lemonade:lemonade-insurance-api
    name: Lemonade Insurance API
    description: A quick and easy way for partners to offer Lemonade homeowners, condo, and renters insurance to their users. Supports quoting, policy creation, and payment, either through the Maya bot drop-in or via direct flow control. Public OpenAPI is not currently published; documentation is available behind the Lemonade developer portal.
    humanURL: https://www.lemonade.com/api
    tags:
      - Insurance
      - Quotes
      - Policies
      - Payments
    properties:
      - url: https://www.lemonade.com/api
        type: Documentation
      - url: https://api-doc-portal.lemonade.com/
        type: Documentation
      - url: https://www.lemonade.com/blog/introducing-lemonade-insurance-api/
        type: Announcement
common:
  - url: https://www.lemonade.com/
    type: Website
  - url: https://www.lemonade.com/api
    type: Documentation
  - url: https://api-doc-portal.lemonade.com/
    type: DeveloperPortal
  - url: https://www.lemonade.com/blog/
    type: Blog
  - url: https://www.lemonade.com/faq
    type: FAQ
  - url: https://www.lemonade.com/partners-program
    type: Partners
  - url: https://www.lemonade.com/api-terms
    type: TermsOfService
  - url: https://www.lemonade.com/privacy-policy
    type: PrivacyPolicy
  - url: https://github.com/lemonade-hq
    type: GitHub
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
