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
artifact_total: 0
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/colfaxcorporation
- group: other
  title: ''
  type: Successor (Enovis)
  url: https://enovis.com
- group: other
  title: ''
  type: Successor (ESAB)
  url: https://www.esabcorporation.com
- group: other
  title: ''
  type: History
  url: https://enovis.com/corporate-info/our-company/history
- group: other
  title: ''
  type: Spin-Off Announcement
  url: https://ir.enovis.com/news-releases/news-release-details/enovis-formerly-colfax-completes-spin-esab-corporation
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Enovis
coverage:
  checked: '2026-09-05'
  detail: Colfax Corporation stopped existing on 2022-04-04 — it spun off ESAB and renamed itself Enovis — and its corporate domain colfaxcorp.com is now a mail-only shell run by ESAB that publishes no A record at all, so every HTTP probe fails at DNS; the only surviving Colfax-branded host, ir.colfaxcorp.com, is a pre-2022 press-release archive on Q4's IR platform that returns 403 to every non-browser client including /robots.txt.
  evidence:
  - status: 0
    url: https://colfaxcorp.com/
  - status: 0
    url: https://colfaxcorp.com/.well-known/security.txt
  - status: 403
    url: https://ir.colfaxcorp.com/robots.txt
  - status: 403
    url: https://ir.colfaxcorp.com/.well-known/agent-card.json
  - status: 200
    url: https://enovis.com/corporate-info/our-company/history
  reason: defunct
  state: none
created: '2025-03-23'
description: 'Colfax Corporation was a diversified global manufacturer founded in 1995 in Richmond, Virginia by Steven and Mitchell Rales. In April 2022, Colfax completed the spin-off of its fabrication technology business as ESAB Corporation (NYSE: ESAB) and renamed itself Enovis Corporation (NYSE: ENOV), refocusing on specialty medical technologies. The Colfax brand and corporate entity no longer exists as an operating company. This profile is preserved for historical reference and routes to the two successor entities. No Colfax-branded developer APIs were ever published; any successor APIs would fall under Enovis or ESAB.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/colfax.png
layout: provider
modified: '2026-09-05'
name: Colfax Corporation (Historical)
nav: Providers
network: true
overview: Colfax Corporation (Historical) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fabrication Technology, Historical, Industrial, Medical Technology, and Spin-Off.
press:
- date: '2026-05-25'
  title: 'Equitable Algorithms: How Human-Centered AI Can ...'
  url: https://www.relmanlaw.com/media/news/1090_2021.05_Hayes_HFSC_AI_Task_Force_Testimony.pdf
- date: '2026-05-25'
  title: HOW HUMAN-CENTERED AI CAN ADDRESS SYSTEMIC ...
  url: https://www.govinfo.gov/content/pkg/CHRG-117hhrg44838/html/CHRG-117hhrg44838.htm
- date: '2026-05-25'
  title: LDF, SBPC, and Upstart Announce Final Monitorship ...
  url: https://www.naacpldf.org/press-release/ldf-sbpc-and-upstart-announce-final-monitorship-report-on-ai-and-fair-lending/
- date: '2026-05-25'
  title: Disparate Impact as Uniquely Relevant in the Age of AI
  url: https://civilrights.org/disparate-impact-age-of-ai/
- date: '2026-05-25'
  title: Untether AI Partners with Colfax International to Provide ...
  url: https://www.businesswire.com/news/home/20210204005099/en/Untether-AI-Partners-with-Colfax-International-to-Provide-Peak-Performance-in-AI-Edge-Servers
random_paper: 7
screenshot: https://raw.githubusercontent.com/api-evangelist/colfax/refs/heads/main/screenshots/colfax-2026-06-20T174743.png
slug: colfax
tags:
- Fabrication Technology
- Historical
- Industrial
- Medical Technology
- Spin-Off
---
