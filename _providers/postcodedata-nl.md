---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 1
apis:
- description: Provide geolocation data based on postcode for Dutch addresses
  name: PostcodeData.nl
  slug: postcodedatanl
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postcodedata-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://api.postcodedata.nl/v1/postcode/?postcode=1211EP&streetnumber=60&ref=domeinnaam.nl&type=json
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Provide geolocation data based on postcode for Dutch addresses
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postcodedata-nl.png
layout: provider
modified: '2026-05-28'
name: PostcodeData.nl
nav: Providers
network: true
overview: PostcodeData.nl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding and Public APIs.
random_paper: 5
screenshot: https://raw.githubusercontent.com/api-evangelist/postcodedata-nl/refs/heads/main/screenshots/postcodedata-nl-2026-06-20T191951.png
security:
- kind: domain-security
  name: Postcodedata Nl Domain Security
  slug: postcodedata-nl-domain-security
  summary_line: DNSSEC
slug: postcodedata-nl
tags:
- Geocoding
- Public APIs
website: http://api.postcodedata.nl/v1/postcode/?postcode=1211EP&streetnumber=60&ref=domeinnaam.nl&type=json
---
