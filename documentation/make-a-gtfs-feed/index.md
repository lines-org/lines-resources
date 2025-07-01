# LineS Documentation - Make a GTFS feed

- [LineS Documentation - Welcome          ]( /documentation/index.md)
- [LineS Documentation - Portal           ]( /documentation/portal/index.md)
- [LineS Documentation - API              ]( /documentation/api/index.md)
- [LineS Documentation - Make a GTFS feed ]( /documentation/make-a-gtfs-feed/index.md)
  - [Introduction to GTFS                 ]( /documentation/make-a-gtfs-feed/index.md#introduction-to-gtfs)
  - [Toolkits                             ]( /documentation/make-a-gtfs-feed/index.md#toolkits)
  - [Examples                             ]( /documentation/make-a-gtfs-feed/index.md#examples)
  - [Using the Portal and API             ]( /documentation/make-a-gtfs-feed/index.md#using-the-portal-and-api)

In this section, you will find information on how to create a GTFS feed that can be later used in the LineS Portal and API.

## Introduction to GTFS

In 2006, a public transport data exchange format named [GTFS](https://gtfs.org) (short for General Feed Transit Specification) was released to the public, originating from a collaboration between the transport operator TriMet in Portland (Oregon) and Google. Its simplicity led to a wide adoption and popularity among the community of transport operators, developers, and other stakeholders, which create and maintain publicly available GTFS feeds and contribute to the standard. It is currently divided into two major implementations, GTFS Schedule and GTFS Realtime, the latter being an extension of the prior with real-time information. Since 2019, it is managed by [MobilityData](https://mobilitydata.org), a non-profit organization aimed to further maintain GTFS with the help of the community.

Here, we will focus on GTFS Schedule (or just GTFS), in particular the entities that are supported by the API and correspond to the minimum required to create a functional GTFS feed: `agency.txt`, `calendar.txt`, `calendar_dates.txt`, `routes.txt`, `stops.txt`, `stop_times.txt`, and `trips.txt`.

In case of doubt regarding the GTFS format, check out the [GTFS Reference](https://gtfs.org/documentation/schedule/reference/).

## Toolkits

Here we present a few toolkits that can help you extract data from various sources, that can be used to create a GTFS feed.

### Libraries

- **PDF Wrapper** (Python): designed to extract tabled information from PDF files, based on the [PDF Plumber](https://pypi.org/project/pdfplumber) library ([link](https://github.com/lines-org/lines-resources/blob/main/toolkits/python/libraries/pdf_wrapper.py)).
- **STePP Wrapper** (Python): designed to extract data from geographic databases, in particular the [STePP](https://www.stepp.pt/sigweb/) database ([link](https://github.com/lines-org/lines-resources/blob/main/toolkits/python/libraries/stepp_wrapper.py)).

### Models

- **GTFS Entities** (Python): a set of models that represent the GTFS entities and can be used for their programmatic creation ([link](https://github.com/lines-org/lines-resources/tree/main/toolkits/python/models/gtfs)).

## Examples

### From PDF to GTFS - Demo for Aveiro Bus Line 11 (Python)

Learn how to extract a schedule from a PDF file and the location of stops from a geographic database, and create a valid GTFS feed from it. 
  - Used **PDF Wrapper** and **STePP Wrapper** toolkits to extract the data.
  - Used **GTFS Entities** models to create the GTFS feed.
  - All files available in the repository ([link](https://github.com/lines-org/lines-resources/tree/main/demo/python/from-pdf-to-gtfs)).
  - Step-by-step instructions in the Jupyter Notebook `src/demo.ipynb` ([link](https://github.com/lines-org/lines-resources/blob/main/demo/python/from-pdf-to-gtfs/src/demo.ipynb)).

## Using the Portal and API

Once you have created your GTFS feed, you can add it to the Portal or API to make it available for use to everyone.

- For the **Portal**, see the [Portal documentation](/documentation/portal/index.md) to create and upload your feed in ZIP format.
- For the **API**, see the [API documentation](/documentation/api/index.md) to create and upload your feed, either in ZIP format or using the entity endpoints.