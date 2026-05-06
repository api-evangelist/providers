---
name: Google Cloud Talent Solution
description: Google Cloud Talent Solution provides a job search and talent acquisition platform that leverages machine learning to match job seekers with relevant opportunities. It offers job posting management, candidate profile search, and intelligent job recommendations for enterprises and job boards.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-talent-solution/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - Google Cloud
  - Jobs
  - Machine Learning
  - Recruitment
  - Search
  - Talent
apis:
  - name: Google Cloud Talent Solution API
    description: The Cloud Talent Solution API enables job search, job posting management, company profiles, and tenant administration for building intelligent talent acquisition applications.
    humanURL: https://cloud.google.com/solutions/talent-solution
    baseURL: https://jobs.googleapis.com
    tags:
      - Jobs
      - Recruitment
      - Search
      - Talent
    properties:
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: JSONSchema
        url: json-schema/job.json
      - type: JSONLDContext
        url: json-ld/context.jsonld
common:
  - type: GettingStarted
    url: https://cloud.google.com/solutions/talent-solution/docs
  - type: Pricing
    url: https://cloud.google.com/solutions/talent-solution/pricing
  - type: JSONLDContext
    url: json-ld/context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
