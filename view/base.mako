<!doctype html>
<html>
    <head>
        <title>
        <%block name="title">
            Civil Engineering Toolbox
        </%block>
        </title>
        <!-- CSS -->
        <link href="/static/bootstrap/css/bootstrap.min.css"
              rel="stylesheet" type="text/css" />
        <link href="/static/bootstrap/css/bootstrap.min.css"
              rel="stylesheet" type="text/css" />
        <link href="/static/font-awesome/css/font-awesome.min.css"
              rel="stylesheet" type="text/css" />
        <link href="/static/jquery-ui/jquery-ui.min.css"
              rel="stylesheet" type="text/css" />
        <link href="/static/jquery-ui/jquery-ui.theme.min.css"
              rel="stylesheet" type="text/css" />
        <link href="/static/css/custom.css"
              rel="stylesheet" type="text/css" />
        <style>
        @font-face {
          font-family: 'PT Sans';
          font-style: normal;
          font-weight: 400;
          src: local('PT Sans'), local('PTSans-Regular'), url(/static/css/pt-sans.woff) format('woff');
        }
        </style>
        <%block name="css">
        </%block>

        <!-- JS -->
        <script src="/static/jquery-ui/external/jquery/jquery.min.js"></script>
        <script src="/static/bootstrap/js/bootstrap.min.js"></script>
        <script src="/static/js/jquery-table-sorter.min.js"></script>
        <script src="/static/js/jquery-floatThead.min.js"></script>
        <script src="/static/jquery-ui/jquery-ui.min.js"></script>
        <script src="/static/js/global.js"></script>
        <%block name="javascript">
        </%block>
    </head>
    <body>
        <div class="container-fluid">
            <%include file="navigation.mako"/>
            <div class="row content">
                <div class="row col-md-10 col-md-offset-1">
                    <%block name="content">
                        No content
                    </%block>
                </div>
            </div>
            <div class="row footer">
                <div class="col-md-4 col-md-offset-6">
                    <br>
                </div>
            </div>
        </div>
    </body>
</html>