---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Orakl Agentic Access
  operation_count: 11
  slug: orakl-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 1
apis:
- baseURL: https://www.orakl-oncology.com
  baseurl_source: declared
  description: Resource 'CommonContent' operations.
  name: Orakl CommonContent API
  slug: orakl-commoncontent-api
- baseURL: https://www.orakl-oncology.com
  baseurl_source: declared
  description: CustomForms describe each node structure family, They are mandatory before creating any Node.
  name: Orakl CustomForm API
  slug: orakl-customform-api
- baseURL: https://www.orakl-oncology.com
  baseurl_source: declared
  description: Folders entity represent a directory on server with datetime and naming.
  name: Orakl Folder API
  slug: orakl-folder-api
- baseURL: https://www.orakl-oncology.com
  baseurl_source: declared
  description: The Login Check API from Orakl — 1 operation(s) for login check.
  name: Orakl Login Check API
  slug: orakl-login-check-api
- baseURL: https://www.orakl-oncology.com
  baseurl_source: declared
  description: NodesSources store Node content according to a translation and a NodeType.
  name: Orakl NodesSources API
  slug: orakl-nodessources-api
- baseURL: https://www.orakl-oncology.com
  baseurl_source: declared
  description: Page node-source entity.
  name: Orakl Page API
  slug: orakl-page-api
- baseURL: https://www.orakl-oncology.com
  baseurl_source: declared
  description: Tags are hierarchical entities used to qualify Nodes.
  name: Orakl Tag API
  slug: orakl-tag-api
- baseURL: https://www.orakl-oncology.com
  baseurl_source: declared
  description: Translations describe language locales to be used by Nodes, Tags, UrlAliases and Documents.
  name: Orakl Translation API
  slug: orakl-translation-api
- baseURL: https://www.orakl-oncology.com
  baseurl_source: declared
  description: Resource 'WebResponse' operations.
  name: Orakl WebResponse API
  slug: orakl-webresponse-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Orakl Oncology public website CommonContent API
  slug: open-orakl-commoncontent-api
- collection_type: open
  name: Orakl Oncology public website CommonContent CustomForm API
  slug: open-orakl-customform-api
- collection_type: open
  name: Orakl Oncology public website CommonContent Folder API
  slug: open-orakl-folder-api
- collection_type: open
  name: Orakl Oncology public website CommonContent Login Check API
  slug: open-orakl-login-check-api
- collection_type: open
  name: Orakl Oncology public website CommonContent NodesSources API
  slug: open-orakl-nodessources-api
- collection_type: open
  name: Orakl Oncology public website CommonContent Page API
  slug: open-orakl-page-api
- collection_type: open
  name: Orakl Oncology public website CommonContent Tag API
  slug: open-orakl-tag-api
- collection_type: open
  name: Orakl Oncology public website CommonContent Translation API
  slug: open-orakl-translation-api
- collection_type: open
  name: Orakl Oncology public website CommonContent WebResponse API
  slug: open-orakl-webresponse-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/orakl-website-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orakl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.orakl-oncology.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.orakl-oncology.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.orakl-oncology.com/api/docs.jsonld
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orakl-oncology.com/legals
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orakl-oncology.com/legals
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orakloncology/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orakl-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orakl-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/orakl-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/orakl-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orakl-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Orakl Oncology is a Paris-based TechBio company, a spin-off from the Gustave Roussy cancer institute, building an AI-powered drug-development platform that combines one of the largest biobanks of patient tumor avatars (organoids) with deep clinical and omics data and machine learning to predict how individual patients will respond to new cancer drug candidates. Its commercial products O-Predict and O-Validate deliver actionable response predictions to drug developers across clinical trials. This API Evangelist profile documents the public website API (an API Platform / Roadiz headless-CMS Hydra + JSON-LD surface with JWT authentication) that powers orakl-oncology.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orakl.png
layout: provider
modified: '2026-07-20'
name: Orakl
nav: Providers
network: true
overview: 'Orakl publishes 9 APIs on the [APIs.io](https://apis.io/) network, including CommonContent API, CustomForm API, Folder API, and 6 more. Tagged areas include Company, TechBio, Oncology, Drug Development, and Artificial Intelligence.


  Orakl''s developer surface includes documentation, API reference, authentication, and 11 more developer resources.'
random_paper: 12
screenshot: https://raw.githubusercontent.com/api-evangelist/orakl/refs/heads/main/screenshots/orakl-2026-08-07T190829.png
security:
- kind: authentication
  name: Orakl Authentication
  slug: orakl-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Orakl Domain Security
  slug: orakl-domain-security
  summary_line: TLSv1.3 · HSTS
slug: orakl
tags:
- Company
- TechBio
- Oncology
- Drug Development
- Artificial Intelligence
- Machine-Learning
- Healthcare
- Biotechnology
- Precision Medicine
- Cancer Research
- Content Management
- JSON-LD
website: https://www.orakl-oncology.com/
---
