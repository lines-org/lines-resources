# LineS Documentation - Portal

- [LineS Documentation - Welcome          ]( /documentation/index.md)
- [LineS Documentation - Portal           ]( /documentation/portal/index.md)
  - [Creating an account                  ]( /documentation/portal/index.md#creating-an-account)
  - [Logging in and out                   ]( /documentation/portal/index.md#logging-in-and-out)
  - [Managing your account                ]( /documentation/portal/index.md#managing-your-account)
  - [Using the personal dashboard         ]( /documentation/portal/index.md#using-the-personal-dashboard)
  - [Browse and view available feeds      ]( /documentation/portal/index.md#browse-and-view-available-feeds)
  - [Read the documentation               ]( /documentation/portal/index.md#read-the-documentation)
- [LineS Documentation - API              ]( /documentation/api/index.md)
- [LineS Documentation - Make a GTFS feed ]( /documentation/make-a-gtfs-feed/index.md)

In this section, you will find information on how to use the LineS Portal, which is the web interface for managing your GTFS feeds.

## Creating an account

You need to create an account in the Portal to be able to manage your feeds.

- Click on `Login` (top right corner) and then select `Sign Up`.
- Provide your email and a strong password - these will be your login credentials.
- You will receive a confirmation email with a link to activate your account. Check your spam folder if you don't see it in your inbox.

> You must use the link in the confirmation email to activate your account, only then you will be able to log in to the Portal.

## Logging in and out

You can log in to the Portal using the email and password you provided during sign up.

- Click on `Login` (top right corner).
- Insert your email and password, then click `Login`.

Once you are done, you can log out of the Portal and your session will be terminated.

- Click on the `User Icon` (top right corner) and select `Logout` (dropdown menu).

## Managing your account

You can manage your account settings in the Portal by clicking the `User Icon` (top right corner) and selecting `Account` (dropdown menu).

> You must be logged in to access your account page.

On the account page, you can:

- **(Re)generate your API key -** used to authenticate your requests to the API.

- **Change your password -** if you want to update it.
  
You can log out of your account by clicking the `User Icon` in the top right corner and selecting `Logout` from the dropdown menu.

## Using the personal dashboard

The dashboard is your personal space in the Portal. It allows you to create and manage your feeds, as well as your API key.

You can access the dashboard in two ways:

- Click on `Dashboard` (navigation bar).
- Click on the `User Icon` (top right corner) and select `Dashboard` (dropdown menu).

On the dashboard page, you can:

- **(Re)generate your API key -** used to authenticate your requests to the API.

- **Create a new feed -** by providing a unique feed ID (among all feeds in Portal), a name (that is human-readable), and an optional description (if name is not descriptive enough). 
  
  A feed from Aveiro Bus could be created as follows: `id:aveiro-bus`, `name:Aveiro Bus` and `description:Buses operated by Aveiro Bus in Aveiro, Portugal`.

  > The feed ID **CANNOT** be changed later! It is used to identify the feed in the API.

- **View your feeds -** all the feeds you have created or are an editor of will be listed on the dashboard. You can see the feed ID, name, description, and the date it was created. You can click on `More Actions` in a feed to go to the page dedicated to that feed (see [Browse and view available feeds](#browse-and-view-available-feeds)).

- **Update the metadata of a feed -** by clicking the `Pencil Icon` of the feed you want to edit. You can only change the name and description of the feed.

- **Delete a feed -** by clicking the `Trash Icon` of the feed you want to delete. This will permanently delete the feed and all its data, so be careful!

- **Add an editor to a feed -** by clicking on `Add Editor` of the feed you would like to share with another user. You need to provide the email address of the editor, which needs to have an account in the Portal.

  An editor of a feed can perform many of the same actions as its creator (e.g., upload a new version of the feed); however, an editor of a feed **CANNOT**:
  - Create it (on API).
  - Update its name and description (on Portal).
  - Delete it (on Portal and API).
  - Add other editors to it (on Portal).

  > The editor can use its own API key to authenticate requests in the API directed to the feed it is an editor of.


## Browse and view available feeds

Click on `Feeds` (navigation bar) to view all the feeds available in the Portal.

If you click on `More Actions` on a feed, you will be redirected to the feed page, where you can:

- **View the feed metadata -** such as the feed ID, name, description, and the date it was created. This information is displayed at the top of the page.

- **Download the feed -** by clicking `Download`. The file will be downloaded to your device, and will follow the GTFS specification - that is, a ZIP file containing CSV files with the feed data.

- **View the feed report -** generated by the [Canonical GTFS Validator](https://github.com/MobilityData/gtfs-validator), by clicking `View Report`. The results are then displayed on the page to help you identify any issues with the feed. You can click on `Download Report` to download the report as it is (HTML file).

- **View the history of changes -** which shows all the changes made to the feed in chronological order. This includes the author and description of each change, as well as the time it was made and its associated commit hash. You can click on `View Changes` to see the exact changes made to the feed files in each commit.

If you are the creator or an editor of the feed, you can also:

- **Upload a new version of the feed -** by either draging the GTFS feed in ZIP format into the designated area, or clicking `Select a File` to choose a file from your device.

- **Revert changes -* by clicking on `Revert` next to a commit in the history to revert all the changes introduced by it. Be careful, as this will create a new commit that undoes the changes made in the selected commit!

## Read the documentation

You can read this documentation by clicking on `Documentation` (navigation bar).

This documentation as a whole provides detailed information on how to use the Portal and API. It also includes guides on how to transform public transport data into the GTFS format, along with examples and toolkits to help you get started.