---
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://circlesup.com/
- group: company
  title: ''
  type: About
  url: https://circlesup.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://circlesup.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://circlesup.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://circlesup.typeform.com/to/e5q9ZYmq
- group: start
  title: ''
  type: Login
  url: https://circlesup.com/app/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://circlesup.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://circlesup.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/7chairs
- group: auth
  title: ''
  type: DomainSecurity
  url: security/7chairs-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/7chairs-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Circles is a direct-to-consumer subscription mental-health app with no developer program at all - circlesup.com/developers/ and circlesup.com/api/ are soft-404s from the WordPress catch-all, and the api.circlesup.com host that does exist answers every path, including its root, with an nginx 503 page rather than any documented surface.
  evidence:
  - status: 200
    url: https://circlesup.com/developers/
  - status: 200
    url: https://circlesup.com/api/
  - status: 503
    url: https://api.circlesup.com/openapi.json
  - status: 200
    url: https://app.circlesup.com/openapi.json
  - status: 200
    url: https://circlesup.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 'Circles (legal entity 7Chairs Ltd, founded 2020 by Irad Eichler and Guy Winch) is a consumer digital mental-health company operating an online emotional support platform at circlesup.com. It runs live, facilitator-led audio and video support groups plus peer chat for people working through narcissistic abuse, toxic relationships, breakups, divorce, grief, anxiety and stress, delivered through iOS and Android apps and a web app at app.circlesup.com. It is a direct-to-consumer subscription service, not a developer platform: as of the 2026-09-05 enrichment pass the company publishes no developer portal, no API documentation and no machine-readable contract, and its api.circlesup.com host answers every request with an HTTP 503 edge page.'
image: https://circlesup.com/wp-content/uploads/2023/03/image-96.png
layout: provider
modified: '2026-09-05'
name: Circles - Online Group Support
nav: Providers
network: true
overview: 'Circles - Online Group Support is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mental Health, Health Care, Wellness, and Consumer Applications.


  Circles - Online Group Support''s developer surface includes engineering blog, support, signup flow, and 8 more developer resources.'
random_paper: 17
security:
- kind: domain-security
  name: 7Chairs Domain Security
  slug: 7chairs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 7chairs
tags:
- Company
- Mental Health
- Health Care
- Wellness
- Consumer Applications
- Support Groups
- Mobile Applications
- Subscription
website: https://circlesup.com/
---
