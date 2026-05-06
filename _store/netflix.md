---
aid: netflix
name: Netflix
description: Netflix is a streaming entertainment service operating one of the world's largest content delivery networks. While Netflix does not publish a general public consumer API, it operates partner programs including Open Connect for ISP CDN integration and device certification programs for manufacturers embedding the Netflix application.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CDN
  - Content Delivery
  - Device Certification
  - Entertainment
  - Media
  - Netflix
  - Open Connect
  - Streaming
url: https://raw.githubusercontent.com/api-evangelist/netflix/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: netflix:netflix-open-connect
    name: Netflix Open Connect
    description: Netflix Open Connect is the purpose-built content delivery network that delivers Netflix streaming traffic. The Open Connect program provides partner ISPs with embedded appliances and peering arrangements to localize Netflix traffic and improve member streaming quality.
    humanURL: https://openconnect.netflix.com/
    tags:
      - CDN
      - ISP
      - Open Connect
      - Peering
      - Streaming
    properties:
      - type: Documentation
        url: https://openconnect.netflix.com/en/
      - type: Deployment Guide
        url: https://openconnect.netflix.com/en/deployment-guide/
      - type: Peering
        url: https://openconnect.netflix.com/en/peering/
      - type: Contact
        url: https://openconnect.netflix.com/en/contact-us/
  - aid: netflix:netflix-partner-help-center
    name: Netflix Partner Help Center
    description: The Netflix Partner Help Center provides resources for device manufacturers, integrators, and content partners. It documents device certification requirements, integration specifications, and support processes for partners building Netflix-enabled products.
    humanURL: https://partnerhelp.netflixstudios.com/
    tags:
      - Certification
      - Device Integration
      - Partners
    properties:
      - type: Documentation
        url: https://partnerhelp.netflixstudios.com/
common:
  - type: Website
    url: https://www.netflix.com
  - type: Open Connect
    url: https://openconnect.netflix.com/
  - type: Tech Blog
    url: https://netflixtechblog.com/
  - type: GitHub Organization
    url: https://github.com/Netflix
  - type: Partner Help Center
    url: https://partnerhelp.netflixstudios.com/
  - type: Jobs
    url: https://jobs.netflix.com/
  - type: About
    url: https://about.netflix.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
