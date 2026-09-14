---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 3
apis:
- description: Partner/OEM-gated cloud AI surface behind Second Opinion. When an imaging partner uploads a bitewing, periapical, panoramic, or CBCT radiograph, Pearl's cloud computer-vision service analyzes it and r
  name: Pearl Second Opinion Image Analysis API
  slug: pearl-dental-second-opinion-image-analysis-api
- description: Practice Intelligence pairs Pearl's diagnostic AI with full practice-management-system data to surface clinical quality, financial performance, appointment compliance, case acceptance, and per-provide
  name: Pearl Practice Intelligence Analytics API
  slug: pearl-dental-practice-intelligence-analytics-api
- description: 'The integration/enablement layer through which Pearl is provisioned inside third-party imaging and practice management systems - including as an authorized vendor in the Henry Schein One API Exchange '
  name: Pearl PMS Integration Exchange API
  slug: pearl-dental-pms-integration-exchange-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pearl-dental-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hellopearl
- group: company
  title: ''
  type: Website
  url: https://hellopearl.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.hellopearl.com
- group: start
  title: ''
  type: Portal
  url: https://management.hellopearl.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/pearl-dental-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://hellopearl.com/blog
created: '2026-07-05'
description: Pearl is a dental AI computer-vision company whose FDA-cleared products - Second Opinion (real-time pathology and restorative detection on 2D and 3D dental radiographs), Practice Intelligence (clinical and operational analytics over full practice-management-system data), and Precheck (AI insurance claim review) - are delivered by embedding Pearl's cloud AI into third-party imaging and practice management software rather than through a public, self-serve developer API. Pearl integrates natively with 40+ imaging/PMS platforms (DEXIS, Carestream, Planmeca Romexis, Dentsply Sirona Sidexis, Apteryx XVWeb, MiPACS, Open Dental, Dentrix, Eaglesoft, Curve, Denticon, Software of Excellence EXACT) and is an authorized vendor in the Henry Schein One API Exchange. There is no publicly documented, self-signup Pearl developer API, SDK, or OpenAPI reference; API access is partner/OEM-gated and arranged through Pearl's integrations and sales teams. The API surfaces below are modeled from Pearl's
  public product descriptions and integration architecture, not from published Pearl API reference documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pearl-dental.png
layout: provider
modified: '2026-07-05'
name: Pearl
nav: Providers
network: true
overview: 'Pearl publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Dental, Computer-Vision, Radiology, and Medical Imaging.


  Pearl''s developer surface includes documentation, developer portal, engineering blog, and 4 more developer resources.'
plans:
- name: Pearl Dental Plans Pricing
  plan_count: 0
  slug: pearl-dental-plans-pricing
random_paper: 12
screenshot: https://raw.githubusercontent.com/api-evangelist/pearl-dental/refs/heads/main/screenshots/pearl-dental-2026-08-07T191728.png
security:
- kind: domain-security
  name: Pearl Dental Domain Security
  slug: pearl-dental-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pearl-dental
tags:
- Artificial Intelligence
- Dental
- Computer-Vision
- Radiology
- Medical Imaging
- Pathology Detection
- Healthcare
- Partner Gated
website: https://hellopearl.com
---
