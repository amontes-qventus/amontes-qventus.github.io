---
theme: dashboard
title: Plotly Example
toc: false
---


<h2>Changes Admitting Service Class</h2>

<div id="tester" style="width:600px;height:250px;"></div>
<div id="myDiv" style="width:600px;height:250px;"></div>
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

    // Create the visualization
    function createSankeyDiagram(data) {
    // Assuming data has columns like 'source', 'target', and 'value'
    const plotData = [{
        type: "sankey",
        orientation: "h",
        node: {
        pad: 15,
        thickness: 30,
        line: {
            color: "black",
            width: 0.5
        },
        label: [...new Set([...data.map(d => d.source), ...data.map(d => d.target)])],
        color: "blue"
        },
        link: {
            source: data.map(d => d.source),
            target: data.map(d => d.target),
            value: data.map(d => d.value)
        }
    }];

    const layout = {
        title: "Hospital Service Changes Flow",
        font: {
        size: 10
        },
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
    const processed_data = hospital_change_admitting_service_class.map(row => ({
    source: row.source,  // adjust field names as needed
    target: row.target,  // adjust field names as needed
    value: row.value            // adjust field names as needed
    }));
    createSankeyDiagram(processed_data)
    
    const unique_labels = [...new Set([...processed_data.map(d => d.source), ...processed_data.map(d => d.target)])]
    const source = processed_data.map(d => d.source)
    const target = processed_data.map(d => d.target)
    const value = processed_data.map(d => d.value)

    console.log(processed_data)
    console.log(unique_labels)
    console.log(source)
    console.log(target)
    console.log(value)

    
```


