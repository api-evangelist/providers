---
aid: bureau-of-indian-affairs
name: Bureau of Indian Affairs
description: The Bureau of Indian Affairs (BIA) is the oldest bureau in the U.S. Department of the Interior. Its mission is to enhance the quality of life, promote economic opportunity, and carry out the federal responsibility to protect and improve the trust assets of American Indians, Indian tribes, and Alaska Natives. The BIA administers services directly or through contracts, grants, and compacts with 574 federally recognized tribes serving approximately 2.5 million people. BIA publishes geospatial datasets, directories, and forms through the Indian Affairs GIS Open Data portal, the Tribal Leader Directory, and official agency websites.
type: Index
x-type: government
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Federal Government
  - GIS
  - ICWA
  - Indigenous
  - Tribal
  - Tribal Governance
  - Trust Assets
url: https://raw.githubusercontent.com/api-evangelist/bureau-of-indian-affairs/refs/heads/main/apis.yml
created: '2024-11-25'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: bureau-of-indian-affairs:bureau-of-indian-affairs
    name: Bureau of Indian Affairs
    description: The Bureau of Indian Affairs is the oldest bureau in the U.S. Department of the Interior, carrying out the federal responsibility to protect and improve trust assets of American Indians, Indian tribes, and Alaska Natives through tribal governance support, law enforcement, economic development, natural resources management, and family services.
    humanURL: https://www.bia.gov/bia
    tags:
      - Federal Government
      - Indigenous
      - Tribal Governance
    properties:
      - type: Website
        url: https://www.bia.gov/bia
      - type: Documentation
        url: https://www.bia.gov/bia
      - type: Leadership
        url: https://www.bia.gov/bia/leadership
    x-features:
      - Tribal governance and self-determination support
      - Fee-to-Trust Land Acquisitions
      - Law enforcement and justice services
      - Missing and Murdered Indigenous People (MMIP) Unit
      - Indian Child Welfare Act (ICWA) administration
      - Tiwahe family-focused programs
      - Emergency management
      - Wildland fire management
    x-use-cases:
      - Tribal policy research and compliance
      - Federal recognition and acknowledgement workflows
      - Natural resources and land management
      - Tribal leader and contact discovery
  - aid: bureau-of-indian-affairs:indian-affairs-gis-open-data
    name: Indian Affairs GIS Open Data
    description: The Indian Affairs GIS Open Data Hub publishes authoritative geospatial datasets as downloadable and machine-readable resources via Esri ArcGIS Hub, including federally recognized tribal boundaries, land areas, ICWA designated agents, and program awards. Each dataset is available as API, GeoJSON, Shapefile, CSV, and KML.
    humanURL: https://biamaps.doi.gov/bogs/datadownload.html
    tags:
      - ArcGIS
      - Geospatial
      - GIS
      - Open Data
      - Tribal Lands
    properties:
      - type: Open Data Hub
        url: https://biamaps.doi.gov/bogs/datadownload.html
      - type: GIS Services
        url: https://biamaps.doi.gov/bogs/arcgis/rest/services
    x-features:
      - Federally Recognized Tribes mapping
      - Tribal Land Area boundaries
      - Indian Reservation boundaries
      - ICWA Designated Agents directory
      - Community Resilience awards data
      - Infrastructure for America (BIL) projects
      - Machine-readable formats (GeoJSON, Shapefile, CSV, KML)
      - ArcGIS REST service endpoints
    x-use-cases:
      - Jurisdictional analysis for tribal lands
      - Environmental impact studies
      - Federal grant planning
      - ICWA compliance and notice
  - aid: bureau-of-indian-affairs:tribal-leader-directory
    name: BIA Tribal Leaders Directory
    description: A searchable directory published by the Bureau of Indian Affairs of elected leaders and contact information for each of the 574 federally recognized tribes, released quarterly as a PDF and via the BIA website.
    humanURL: https://www.bia.gov/service/tribal-leaders-directory
    tags:
      - Directory
      - Tribal
    properties:
      - type: Directory
        url: https://www.bia.gov/service/tribal-leaders-directory
    x-features:
      - Contact information for 574 federally recognized tribes
      - Quarterly publication
      - Searchable and downloadable
    x-use-cases:
      - Tribal consultation outreach
      - Government-to-government engagement
      - Compliance with consultation requirements
  - aid: bureau-of-indian-affairs:bureau-of-indian-education
    name: Bureau of Indian Education
    description: The Bureau of Indian Education (BIE) supports programs serving more than 46,000 students across 183 schools, including BIE-operated and tribally-controlled schools, plus postsecondary institutions, providing culturally relevant education to Indian students.
    humanURL: https://www.bie.edu/
    tags:
      - Education
      - Indigenous
      - Tribal
    properties:
      - type: Website
        url: https://www.bie.edu/
      - type: School Directory
        url: https://www.bie.edu/schools
    x-features:
      - K-12 school system for Indian students
      - Postsecondary institution support
      - Tribally-controlled school grants
      - Early childhood education
    x-use-cases:
      - School finder
      - Grant and funding research
      - Tribal education policy
common:
  - type: Website
    url: https://www.bia.gov/
  - type: Privacy Policy
    url: https://www.bia.gov/privacy-policy
  - type: Accessibility
    url: https://www.doi.gov/accessibility
  - type: FOIA
    url: https://www.bia.gov/foia
  - type: Newsroom
    url: https://www.bia.gov/news
  - type: Contact
    url: https://www.bia.gov/contact-us
  - type: Forms
    url: https://www.bia.gov/forms
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
