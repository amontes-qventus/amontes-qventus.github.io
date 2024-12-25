---
theme: dashboard
title: Plotly Example
toc: false
---

<h2>Changes Admitting Service Class</h2>

<div id="tester" style="display:none;width:600px;height:250px;"></div>
<div id="myDiv" style="display:none;width:600px;height:250px;"></div>
<div id="chart" style="width:800px;height:600px;"></div>

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


```js
    const hospital_change_admitting_service_class = await FileAttachment("./data/hospital_change_admitting_service_class.csv").csv({ typed: true });

    const processed_data_1 = hospital_change_admitting_service_class.map(row => ({
    source: row.source + '_source',  // adjust field names as needed
    target: row.target + '_target',  // adjust field names as needed
    value: row.value            // adjust field names as needed
    }));


    // Create the visualization
    function createSankeyDiagram(data) {
    
    const unique_labels_1 = [...new Set([...data.map(d => d.source ), ...data.map(d => d.target )])]
    const labelToIndex = {};
    unique_labels_1.forEach((label, index) => {
    labelToIndex[label] = index;
    });

    // Assuming data has columns like 'source', 'target', and 'value'
    const plotData = [{
        type: "sankey",
        orientation: "h",
        node: {
            pad: 15,
            thickness: 30,
            line: {
                color: "white",
                width: 1
            },
            label: unique_labels_1,
            color: "#1f77b4"
        },
        link: {
            source: data.map(d => labelToIndex[d.source]),
            target: data.map(d => labelToIndex[d.target]),
            value: data.map(d => d.value),
            color: 'rgba(31, 119, 180, 0.4)'  // Semi-transparent blue links
        }
    }];

    const layout = {
        title: "Hospital Service Changes Flow",
        font: {
            size: 15,
            color: 'white'
        },
        plot_bgcolor: 'rgba(0,0,0,0)',
        paper_bgcolor: 'rgba(0,0,0,0)',
        width: 800,
        height: 600
    };

    return Plotly.newPlot('chart', plotData, layout);
    }

    // Assuming your CSV data looks something like:
    // source,target,value
    // ServiceA,ServiceB,10
    // ServiceB,ServiceC,5
    // etc.

    // Process the data and create the visualization

    createSankeyDiagram(processed_data_1)

```