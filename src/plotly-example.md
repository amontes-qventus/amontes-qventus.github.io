---
theme: dashboard
title: Plotly Example
toc: false
---


<h2>Changes Admitting Service Class</h2>

<div id="tester" style="width:600px;height:250px;"></div>
<div id="myDiv" style="width:600px;height:250px;"></div>

```js
    import Plotly from 'plotly.js-dist-min';

    Plotly.newPlot( 'tester', [{
    x: [1, 2, 3, 4, 5],
    y: [1, 2, 4, 8, 16] }], {
    margin: { t: 0 } } );

    console.log( Plotly.BUILD );

    var trace1 = {
    x: [0, 1, 2, 3, 4],
    y: [1, 5, 3, 7, 5],
    mode: 'lines+markers',
    type: 'scatter'
    };

    var trace2 = {
    x: [1, 2, 3, 4, 5],
    y: [4, 0, 4, 6, 8],
    mode: 'lines+markers',
    type: 'scatter'
    };

    var data = [trace1, trace2];
    var layout = {
    title: {
        text: 'Click Here<br>to Edit Chart Title'
    }
    };

    Plotly.newPlot('myDiv', data, layout, {editable: true});

```




