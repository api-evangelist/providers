---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/academi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://constellis.com/constellis-training-center/
coverage:
  checked: '2026-09-06'
  detail: 'ACADEMI is a retired brand, not a live company - Academi Training Center, LLC was one of seven entities merged into Constellis Holdings in June 2014, and Constellis states on its own site that "Constellis does not operate under the Academi name" - and the domain academi.com is now web-retired: port 443 fails the TLS handshake outright and port 80 returns HTTP 409 with a Cloudflare error-1001 body on every path, while DNS keeps only mail (Proofpoint MX, SPF, DMARC p=reject reporting to itsec@constellis.com).'
  evidence:
  - status: 409
    url: http://academi.com/
  - status: 0
    url: https://academi.com/
  - status: 409
    url: http://academi.com/openapi.json
  - status: 200
    url: https://constellis.com/constellis-training-center/
  - status: 404
    url: https://constellis.com/.well-known/api-catalog
  reason: defunct
  state: none
created: '2026-09-06'
description: 'ACADEMI was the 2011-2014 name of the American private military, security and training company founded on 26 December 1996 in North Carolina by Erik Prince and Al Clark as Blackwater. It was renamed Blackwater Worldwide in October 2007 after the Nisour Square shooting in Baghdad, then Xe Services LLC in February 2009. In December 2010 the training business and its Moyock, North Carolina campus - the largest private training facility in the United States - were bought by USTC Holdings, an investor consortium led by Forte Capital Advisors and Manhattan Strategic Ventures, ending Erik Prince''s involvement, and the company was rebranded ACADEMI in December 2011 under chairman Red McCombs. In June 2014 Academi Training Center, LLC was merged with Triple Canopy, Constellis Ltd., Strategic Social, Tidewater Global Services, National Strategic Protective Services and International Development Solutions to form Constellis Holdings, which Apollo Global Management acquired in September
  2016 and which is headquartered in Herndon, Virginia. The ACADEMI brand was retired in the merger: Constellis states on its own site that "Academi remains part of historical, legal, and contractual records, but Constellis does not operate under the Academi name", and the Moyock campus now trades as the Constellis Training Center. The business sells physical services - firearms, driving, maritime, K-9, UAS/C-UAS and advanced security and military training, protective security details, and logistics and complex program management for United States government customers - not software. It never operated a developer program, public API, SDK, webhook surface or machine-readable API specification, and academi.com no longer serves a website: the domain is retained by Constellis for email only. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-09-06'
name: Academi
nav: Providers
network: true
overview: Academi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defense, Private Military, Security Services, and Physical Security.
random_paper: 15
security:
- kind: domain-security
  name: Academi Domain Security
  slug: academi-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: academi
tags:
- Company
- Defense
- Private Military
- Security Services
- Physical Security
- Training
- Government Contracting
- Logistics
- Program Management
- Acquired
- Brand Retired
website: https://constellis.com/constellis-training-center/
---
