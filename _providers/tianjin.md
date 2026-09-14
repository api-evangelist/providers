---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 6
apis:
- description: The university's own Shibboleth identity provider, and the only credential-free, machine-readable contract anywhere in this profile. https://idp.tju.edu.cn/idp/shibboleth returns HTTP 200 and 14,410 b
  name: Tianjin University Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: shibboleth-idp
- description: 'The same identity provider seen from the federation side. Tianjin University''s IdP is registered in CARSI — the CERNET Authentication and Resource Sharing Infrastructure, registration authority https:'
  name: CARSI / eduGAIN Federation Registration (entity 671640)
  slug: carsi-edugain
- description: Tianjin University is a Crossref member in its own right — member id 34483, DOI prefix 10.55582 — and is also present in the Crossref Open Funder Registry under funder ids 501100004517 and 50110001564
  name: Crossref Membership (member 34483, prefix 10.55582)
  slug: crossref
- description: Tianjin University's Research Organization Registry record — the canonical machine-readable identifier for the institution as an entity, and the join key the other registries in this profile resolve a
  name: ROR Registration (https://ror.org/012tb2g32)
  slug: ror
- description: The library's unified discovery front end at find.lib.tju.edu.cn, reachable from outside the campus network and serving a real single-page application titled 统一检索. It publishes no machine-readable con
  name: TJU Library Unified Discovery (统一检索)
  slug: library-discovery
- description: 'Three university systems resolve into TJU''s own address block but are unreachable from outside the campus network: the institutional repository ir.lib.tju.edu.cn and the library OPAC opac.lib.tju.edu.'
  name: Campus-Network-Gated Systems (repository, OPAC, portal)
  slug: campus-gated-systems
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://en.tju.edu.cn/
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/tianjin-identity-federation.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tianjin-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tianjin-conformance.yml
- group: build
  title: ''
  type: LibraryCatalog
  url: https://find.lib.tju.edu.cn/
- group: company
  title: ''
  type: Blog
  url: https://news.tju.edu.cn/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/TJUBlockchainLab
- group: company
  title: ''
  type: LinkedIn
  url: https://cn.linkedin.com/school/tianjinuniversity/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tianjin-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tianjin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tianjin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tianjin-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Tianjin University (天津大学, TJU) is a national public research university in Tianjin, China, founded in 1895 as Peiyang University and recognised as the oldest modern university in the country. It publishes no public API, no developer portal, no open data portal and no specification of any kind: www.tju.edu.cn returns 404 for robots.txt, llms.txt, .well-known/security.txt and .well-known/openid-configuration, and api., data., open., developer. and dev.tju.edu.cn do not resolve. What it does operate — and this is the finding that separates it from most of this cohort — is its own Shibboleth SAML 2.0 identity provider at idp.tju.edu.cn, on the university''s own CERNET address with no vendor CNAME, registered as entity 671640 in CARSI, China''s national research-and-education identity federation, and visible in eduGAIN since October 2019. Its metadata document is credential-free, machine-readable and genuinely the institution''s own engineering rather than a vendor''s contract running
  under the university''s name. Beyond that the estate is a set of relationships and gated systems: a Crossref membership with its own DOI prefix but only eleven registered DOIs, a ROR registration, a library discovery front end that answers only an SPA shell, and an institutional repository, OPAC and campus portal that resolve into TJU''s own address block but redirect every off-campus request to a soft-403 network notice. There is no DataCite membership and no reachable OAI-PMH endpoint.'
finops:
- name: Tianjin Finops
  service_category: Education
  slug: tianjin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tianjin.png
jsonld:
- class_count: 8
  name: Tianjin Context
  property_count: 3
  slug: tianjin-context
layout: provider
modified: '2026-09-01'
name: Tianjin University
nav: Providers
network: true
overview: 'Tianjin University publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and China.


  The Tianjin University catalog on APIs.io includes 1 JSON-LD context.


  Tianjin University''s developer surface includes authentication, engineering blog, GitHub presence, and 10 more developer resources.'
plans:
- name: Tianjin Plans Pricing
  plan_count: 2
  slug: tianjin-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Tianjin Rate Limits
  slug: tianjin-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/tianjin/refs/heads/main/screenshots/tianjin-2026-06-20T195443.png
security:
- kind: authentication
  name: Tianjin Authentication
  slug: tianjin-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tianjin Domain Security
  slug: tianjin-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: tianjin
tags:
- Education
- Higher Education
- University
- Research
- China
- Tianjin
- Double First Class
- Project 985
- Identity Federation
- Shibboleth
- SAML
- Single Sign-On
- Library
- Research Repository
- Persistent Identifiers
website: https://en.tju.edu.cn/
---
