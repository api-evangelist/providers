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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-financial-domain-security.yml
coverage:
  checked: '2026-09-02'
  detail: The only host recorded for this profile, www.american-financial.com, is a parked domain listed for sale — it CNAMEs to traff-https.hugedomains.com and redirects to hugedomains.com/domain_profile.cfm?d=american-financial.com — so there is no company site, developer portal, or API surface behind this name at all; the Fortune 500 company of a similar name is American Financial Group, profiled separately as american-financial-group.
  evidence:
  - status: 200
    url: https://www.american-financial.com
  - status: 200
    url: https://www.hugedomains.com/domain_profile.cfm?d=american-financial.com
  - status: 404
    url: https://www.american-financial.com/.well-known/agent-card.json
  - status: 302
    url: https://www.american-financial.com/openapi.json
  reason: defunct
  state: none
created: '2024-11-15'
description: 'American Financial is a financial-services profile in the API Evangelist catalog for which no operating company could be resolved on 2026-09-02. The only host ever recorded for it, american-financial.com, is not run by a business: it is a CNAME to traff-https.hugedomains.com and redirects to a HugeDomains "this domain is for sale" listing, so there is no website, no developer program, no documentation and no machine-readable API artifact behind this name. The Fortune 500 insurance and annuities holding company American Financial Group, Inc. (NYSE: AFG, Great American Insurance Group) is a different company and is profiled separately in this catalog as american-financial-group, where its Great American Carrier Services APIs belong.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-financial.png
layout: provider
modified: '2026-09-02'
name: American Financial
nav: Providers
network: true
overview: American Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services and Finance.
random_paper: 4
screenshot: https://raw.githubusercontent.com/api-evangelist/american-financial/refs/heads/main/screenshots/american-financial-2026-06-20T171914.png
security:
- kind: domain-security
  name: American Financial Domain Security
  slug: american-financial-domain-security
  summary_line: TLSv1.3
slug: american-financial
tags:
- Financial-Services
- Finance
---
