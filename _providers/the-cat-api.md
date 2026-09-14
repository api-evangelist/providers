---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: The Cat Api Agentic Access
  operation_count: 17
  slug: the-cat-api-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.thecatapi.com/v1
  baseurl_source: declared
  description: List, search, and retrieve cat breed information.
  name: The Cat API Breeds API
  slug: the-cat-api-breeds-api
- baseURL: https://api.thecatapi.com/v1
  baseurl_source: declared
  description: Retrieve available image categories.
  name: The Cat API Categories API
  slug: the-cat-api-categories-api
- baseURL: https://api.thecatapi.com/v1
  baseurl_source: declared
  description: Manage user favourite cat images.
  name: The Cat API Favourites API
  slug: the-cat-api-favourites-api
- baseURL: https://api.thecatapi.com/v1
  baseurl_source: declared
  description: Search, upload, retrieve, and delete cat images.
  name: The Cat API Images API
  slug: the-cat-api-images-api
- baseURL: https://api.thecatapi.com/v1
  baseurl_source: declared
  description: Cast and manage votes on cat images.
  name: The Cat API Votes API
  slug: the-cat-api-votes-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: The Cat Breeds API
  slug: open-the-cat-api-breeds-api
- collection_type: open
  name: The Cat Breeds Categories API
  slug: open-the-cat-api-categories-api
- collection_type: open
  name: The Cat Breeds Favourites API
  slug: open-the-cat-api-favourites-api
- collection_type: open
  name: The Cat Breeds Images API
  slug: open-the-cat-api-images-api
- collection_type: open
  name: The Cat Breeds Votes API
  slug: open-the-cat-api-votes-api
- collection_type: open
  name: The Cat API
  slug: open-the-cat-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-cat-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-cat-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-cat-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://thecatapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.thecatapi.com/
- group: start
  title: ''
  type: Signup
  url: https://account.thecatapi.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thatapicompany
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/the-cat-api/refs/heads/main/openapi/the-cat-api-openapi.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://thecatapi.com/pricing
created: '2025-01-07'
description: An open, free, read and write API all about cats. Access thousands of cat images, vote, favorite, and explore breed information.
examples:
- key_count: 2
  name: The Cat Api Createvote Example
  slug: the-cat-api-createVote-example
- key_count: 2
  name: The Cat Api Listbreeds Example
  slug: the-cat-api-listBreeds-example
- key_count: 2
  name: The Cat Api Searchimages Example
  slug: the-cat-api-searchImages-example
finops:
- name: The Cat Api Finops
  service_category: API
  slug: the-cat-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-cat-api.png
json_schemas:
- name: Cat API Breed
  property_count: 26
  slug: the-cat-api-breed
- name: Cat API Image
  property_count: 6
  slug: the-cat-api-image
json_structures:
- name: The Cat Api Image Search Structure
  property_count: 0
  slug: the-cat-api-image-search-structure
jsonld:
- class_count: 3
  name: The Cat Api Context
  property_count: 21
  slug: the-cat-api-context
layout: provider
modified: '2026-05-19'
name: The Cat API
nav: Providers
network: true
overview: 'The Cat API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Breeds API, Categories API, Favourites API, and 2 more. Tagged areas include Animals, Cats, Image, and Media.


  The The Cat API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  The Cat API''s developer surface includes authentication, documentation, signup flow, pricing, and 5 more developer resources.'
plans:
- name: The Cat Api Plans Pricing
  plan_count: 3
  slug: the-cat-api-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: The Cat Api Rate Limits
  slug: the-cat-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: The Cat API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: the-cat-api-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: The Cat API API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 7
  slug: the-cat-api-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/the-cat-api/refs/heads/main/screenshots/the-cat-api-2026-06-20T195216.png
security:
- kind: authentication
  name: The Cat Api Authentication
  slug: the-cat-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: The Cat Api Domain Security
  slug: the-cat-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: the-cat-api
tags:
- Animals
- Cats
- Image
- Media
website: https://thecatapi.com/
---
