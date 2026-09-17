---
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/againstgravity/refs/heads/main/security/againstgravity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/againstgravity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://recroom.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://recroom.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://recroom.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://recroom.com/ship-notes
- group: operate
  title: ''
  type: Support
  url: https://recroom.zendesk.com/hc/en-us
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/againstgravity/refs/heads/main/lifecycle/againstgravity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/againstgravity-lifecycle.yml
coverage:
  checked: '2026-09-12'
  detail: Rec Room Inc. (formerly Against Gravity Corp) shut its service down on 2026-06-01 and rec.net on 2026-06-09; its Azure API Management developer portal devportal.rec.net is now a dangling CNAME to the deleted instance rr-apim-prod-001.developer.azure-api.net, and both rec.net and api.rec.net answer TLS alert 40 with no certificate, so the only host still served is the legacy recroom.com Squarespace marketing site, which 404s on every spec and /.well-known/ path.
  evidence:
  - status: 0
    url: https://devportal.rec.net/apis
  - status: 0
    url: https://api.rec.net/swagger/v1/swagger.json
  - status: 0
    url: https://rec.net/
  - status: 404
    url: https://recroom.com/openapi.json
  - status: 404
    url: https://recroom.com/.well-known/api-catalog
  - status: 200
    url: https://recroom.com/
  reason: defunct
  state: none
created: '2026-09-12'
description: 'Against Gravity Corp was the Seattle software company founded in April 2016 by Nick Fajt, Cameron Brown, Dan Kroymann, Bilal Orhan, Josh Wehrly and John Bevis that built Rec Room, a cross-platform social gaming and user-generated-content world for PC, PlayStation, Xbox, Meta Quest, iOS and Android. The company later renamed itself Rec Room Inc. and is tracked in this network under the rec-room record. Rec Room announced on 2026-03-30 that it could not reach profitability, took its game servers offline on 2026-06-01 and shut the rec.net community site down on 2026-06-09. It did run a real developer program: an Azure API Management developer portal at devportal.rec.net issuing subscription keys against api.rec.net. Both are gone — devportal.rec.net is a dangling CNAME to a deleted APIM instance and rec.net / api.rec.net answer TLS handshake_failure with no certificate. Only the legacy Squarespace marketing site at recroom.com is still served, so no live contract remains to harvest.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/againstgravity.png
layout: provider
modified: '2026-09-12'
name: Against Gravity
nav: Providers
network: true
overview: 'Against Gravity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Virtual Reality, Social Platform, and User Generated Content.


  Against Gravity''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 21
security:
- kind: domain-security
  name: Againstgravity Domain Security
  slug: againstgravity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: againstgravity
tags:
- Company
- Gaming
- Virtual Reality
- Social Platform
- User Generated Content
- Metaverse
- Entertainment
- Defunct
website: https://recroom.com
---
