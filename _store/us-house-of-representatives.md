---
aid: us-house-of-representatives
url: https://raw.githubusercontent.com/api-evangelist/us-house-of-representatives/refs/heads/main/apis.yml
apis:
  - aid: us-house-of-representatives:congress-gov-api
    name: Congress.gov API
    tags:
      - Legislation
      - Congress
      - Federal Government
      - Legislative Data
    humanURL: https://www.loc.gov/apis/additional-apis/congress-dot-gov-api/
    properties:
      - url: https://www.loc.gov/apis/additional-apis/congress-dot-gov-api/
        type: Documentation
      - url: https://github.com/LibraryOfCongress/api.congress.gov
        type: GitHub
      - url: https://api.congress.gov/
        type: BaseURL
      - url: https://raw.githubusercontent.com/api-evangelist/us-house-of-representatives/refs/heads/main/openapi/congress-gov-api-openapi.yml
        type: OpenAPI
    description: The Congress.gov API (v3) provides programmatic access to congressional data maintained by the Library of Congress. It offers machine-readable data covering bills, amendments, congressional records, committees, members of Congress, nominations, and treaties. An API key is required and can be obtained from api.data.gov. Responses are available in JSON or XML with a rate limit of 5,000 requests per hour and pagination up to 250 results per request.
  - aid: us-house-of-representatives:propublica-congress-api
    name: ProPublica Congress API
    tags:
      - Legislation
      - Congress
      - Voting Records
      - Campaign Finance
    humanURL: https://projects.propublica.org/api-docs/congress-api/
    properties:
      - url: https://projects.propublica.org/api-docs/congress-api/
        type: Documentation
    description: ProPublica's Congress API provides access to detailed congressional data including member profiles, voting records, bill sponsorship, and committee activity. This third-party API aggregates and enriches congressional data from multiple public sources.
name: US House of Representatives
tags:
  - Federal Government
  - Legislation
  - Congress
  - Legislative Data
  - Bills
  - Members
  - Committees
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-05-03'
position: Consuming
description: The United States House of Representatives is one of the two chambers of the United States Congress, with the other being the Senate. Its main function is to pass federal legislation, which must then be approved by the Senate before it can become law. The House also has the power to impeach government officials, including the President, and to initiate revenue-related bills. Congressional data is made available through the Congress.gov API, a REST API maintained by the Library of Congress that provides access to bills, members, committees, amendments, nominations, and treaties.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
