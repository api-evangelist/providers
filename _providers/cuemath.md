---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-11'
  detail: 'Cuemath ships only a consumer tutoring product: api.cuemath.com returns 404, no developer or docs subdomain resolves at all, and the single HTTP API found on its infrastructure — app.cuemath.com/api — is a session-cookie application backend that Cuemath''s own llms.txt explicitly lists under "API endpoints not meant for public access".'
  evidence:
  - status: 404
    url: https://api.cuemath.com/
  - status: 404
    url: https://www.cuemath.com/openapi.json
  - status: 401
    url: https://app.cuemath.com/api
  - status: 200
    url: https://www.cuemath.com/llms.txt
  - status: 200
    url: https://api.github.com/orgs/cuemath
  reason: no-developer-program
  state: none
created: '2026-08-11'
description: Cuemath is an India-headquartered education technology company founded in 2013 by Manan Khurma that delivers live, one-to-one online math tutoring to students in grades K through 12 across more than 80 countries. Its MathFit framework and LEAP learning platform pair certified tutors with an interactive, gamified curriculum aligned to US Common Core standards, spanning arithmetic, algebra, geometry, pre-calculus, AP calculus and standardized test preparation. Cuemath sells directly to families as a subscription tutoring product; it operates a consumer web and mobile application rather than a developer platform, and publishes no public API, SDK or developer portal.
image: https://d138zd1ktt9iqe.cloudfront.net/static/website-v3/math-fit-teaser-16-9.webp
layout: provider
modified: '2026-08-11'
name: Cuemath
nav: Providers
network: true
random_paper: 47
slug: cuemath
tags:
- Company
- Education
- EdTech
- Online Learning
- Tutoring
- Mathematics
- K-12
- Consumer Application
---
