---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acadarena-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.acadarena.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acadarena.com/privacypolicy
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/acadarenagg
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Arclight-Labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acadarena
- group: company
  title: ''
  type: Twitter
  url: https://x.com/acadarena
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/acadarenagg
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://equityzen.com/company/acadarena
- group: build
  title: ''
  type: Packages
  url: packages/acadarena-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acadarena-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/acadarena-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acadarena-rate-limits.yml
coverage:
  checked: '2026-09-06'
  detail: AcadArena ships student-facing campus gaming programs and a Next.js marketing site with no developer, API or documentation section anywhere in its navigation; the only API hostname it ever named, api.acadarena.com, is now a dangling CNAME to a deleted DigitalOcean app that does not resolve, and the Supabase project the website itself calls rejects anonymous requests.
  evidence:
  - status: 200
    url: https://www.acadarena.com/
  - status: 404
    url: https://www.acadarena.com/llms.txt
  - status: 404
    url: https://www.acadarena.com/.well-known/api-catalog
  - status: 401
    url: https://aatesefpjfdqshisyriz.supabase.co/rest/v1/
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: AcadArena is a Philippine campus gaming and esports company founded in 2019 by Ariane Lim, Kevin Hoang and Justin Banusin, and trades today as a brand owned by AcadArena Digital Education Solutions OPC. It builds student communities around games across high-school and college campuses in the Philippines and Southeast Asia, running the AcadArena Alliance student-club accreditation network, an Incubator that helps students stand up a club on a campus that has none, the Buffs marketplace that supplies loot and sponsorship for campus events, an Alliance for Teachers practice community for moderators and educators, and collegiate competitions. The company has served hundreds of schools, has been the Philippine collegiate licensee for Riot Games titles, and raised a $3.5M seed round. Its public surface is a Next.js marketing site backed by a key-gated Supabase project; AcadArena publishes no developer portal, API reference, SDK or machine-readable contract, and the api.acadarena.com
  hostname it once used now resolves only to a dangling CNAME.
image: https://www.acadarena.com/assets/logo/acadarena_logo.png
layout: provider
modified: '2026-09-06'
name: AcadArena
nav: Providers
network: true
overview: AcadArena is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Esports, Gaming, Education, and Community.
plans:
- name: Acadarena Plans Pricing
  plan_count: 0
  slug: acadarena-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Acadarena Rate Limits
  slug: acadarena-rate-limits
security:
- kind: domain-security
  name: Acadarena Domain Security
  slug: acadarena-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: acadarena
tags:
- Company
- Esports
- Gaming
- Education
- Community
- Events
- Students
- Sponsorship
- Philippines
- Southeast Asia
website: https://www.acadarena.com/
---
