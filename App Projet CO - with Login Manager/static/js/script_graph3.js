Highcharts.theme = {
    colors: ['#7dbaff', '#3b39b3', '#b51fd3', '#ff00aa', '#ff0040', '#fff'],
    chart: {
        backgroundColor: {
            linearGradient: { x1: 0, y1: 0, x2: 1, y2: 1 },
            stops: [
                [0, '#37338a00'],
                [1, '#37338a00']
            ]
        },
        style: {
            fontFamily: '\'Unica One\', sans-serif'
        },
        plotBorderColor: '#606063'
    },
    title: {
        style: {
            color: '#E0E0E3',
            /*textTransform: 'uppercase',*/
            fontSize: '20px'
        }
    },
    subtitle: {
        style: {
            color: '#E0E0E3',
            /*textTransform: 'uppercase'*/
        }
    },
    xAxis: {
        gridLineColor: '#707073',
        labels: {
            style: {
                color: '#E0E0E3'
            }
        },
        lineColor: '#707073',
        minorGridLineColor: '#505053',
        tickColor: '#707073',
        title: {
            style: {
                color: '#A0A0A3'
            }
        }
    },
    yAxis: {
        gridLineColor: '#707073',
        labels: {
            style: {
                color: '#E0E0E3'
            }
        },
        lineColor: '#707073',
        minorGridLineColor: '#505053',
        tickColor: '#707073',
        tickWidth: 1,
        title: {
            style: {
                color: '#A0A0A3'
            }
        }
    },
    tooltip: {
        backgroundColor: 'rgba(0, 0, 0, 0.85)',
        style: {
            color: '#F0F0F0'
        }
    },
    plotOptions: {
        series: {
            dataLabels: {
                color: '#F0F0F3',
                style: {
                    fontSize: '13px'
                }
            },
            marker: {
                lineColor: '#333'
            },
            pointWidth: 40
            
        },
        boxplot: {
            fillColor: '#505053'
        },
        candlestick: {
            lineColor: 'white'
        },
        errorbar: {
            color: 'white'
        }
    },
    legend: {
        backgroundColor: 'rgba(0, 0, 0, 0.0)',
        itemStyle: {
            color: '#E0E0E3'
        },
        itemHoverStyle: {
            color: '#FFF'
        },
        itemHiddenStyle: {
            color: '#606063'
        },
        title: {
            style: {
                color: '#C0C0C0'
            }
        }
    },
    credits: {
        style: {
            color: '#666'
        }
    },
    labels: {
        style: {
            color: '#707073'
        }
    },
    drilldown: {
        activeAxisLabelStyle: {
            color: '#F0F0F3'
        },
        activeDataLabelStyle: {
            color: '#F0F0F3'
        }
    },
    navigation: {
        buttonOptions: {
            symbolStroke: '#DDDDDD',
            theme: {
                fill: '#505053'
            }
        }
    },
    // scroll charts
    rangeSelector: {
        buttonTheme: {
            fill: '#505053',
            stroke: '#000000',
            style: {
                color: '#CCC'
            },
            states: {
                hover: {
                    fill: '#707073',
                    stroke: '#000000',
                    style: {
                        color: 'white'
                    }
                },
                select: {
                    fill: '#000003',
                    stroke: '#000000',
                    style: {
                        color: 'white'
                    }
                }
            }
        },
        inputBoxBorderColor: '#505053',
        inputStyle: {
            backgroundColor: '#333',
            color: 'silver'
        },
        labelStyle: {
            color: 'silver'
        }
    },
    navigator: {
        handles: {
            backgroundColor: '#666',
            borderColor: '#AAA'
        },
        outlineColor: '#CCC',
        maskFill: 'rgba(255,255,255,0.1)',
        series: {
            color: '#7798BF',
            lineColor: '#A6C7ED'
        },
        xAxis: {
            gridLineColor: '#505053'
        }
    },
    scrollbar: {
        barBackgroundColor: '#808083',
        barBorderColor: '#808083',
        buttonArrowColor: '#CCC',
        buttonBackgroundColor: '#606063',
        buttonBorderColor: '#606063',
        rifleColor: '#FFF',
        trackBackgroundColor: '#404043',
        trackBorderColor: '#404043'
    }
};


Highcharts.setOptions(Highcharts.theme);
// Histogram
  Highcharts.chart('container_3', {
      chart: {
          type: 'column'
      },
      title: {
        text: '',
        style: {
            display: 'none'
        }
    },

    exporting: {
        buttons: {
            contextButton: {
                align: 'left',
                verticalAlign: 'top'
            }
        }
    },
    subtitle: {
        text: '',
        style: {
            display: 'none'
        }
    },
      xAxis: {
          categories: ['0 %', '10 %', '20 %', '30 %', '40 %', '50 %', '60 %', '70 %', '80 %', '90 %']
      },
      
      yAxis:{
          title: '',
          min: 0,
          alignTicks: false,
          tickInterval: 15,
          labels: {
                  formatter: function() {
                      return '';
                  },
          }
      },
  
      credits: {
          enabled: true
      },
      series: [{
          
          name:'Faux Negatifs',
              data: data_False,
              color:'#ee248286'
      },{     
              name:'Vrais Positifs',
              data: data_True,
              color:'#2493ee86'
      }],
  });

  Highcharts.chart('container_4', {
    chart: {
        zoomType: 'x'
    },
    title: {
        text: '',
        style: {
            display: 'none'
        }
    },
    subtitle: {
        text: '',
        style: {
            display: 'none'
        }
    },
    exporting: {
        buttons: {
            contextButton: {
                align: 'right',
                verticalAlign: 'top'
            }
        }
    },
    xAxis: {
        type: 'number',
        title: {
            text: 'Precision'
        },
    },
    yAxis: {
        title: {
            text: 'Recall'
        },
        min: 0,
        max: 1,
        alignTicks: false,
        tickInterval: 0.2,
    },
    legend: {
        enabled: false
    },
    plotOptions: {
        area: {
            fillColor: {
                linearGradient: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 1
                },
                stops: [
                    [0, Highcharts.getOptions().colors[0]],
                    [1, Highcharts.color(Highcharts.getOptions().colors[1]).setOpacity(0).get('rgba')]
                ]
            },
            marker: {
                radius: 2
            },
            lineWidth: 1,
            states: {
                hover: {
                    lineWidth: 1
                }
            },
            threshold: null
        }
    },

        series: [{
            type: 'area',
            data: data_curve
        }]
    });

    Highcharts.chart('container_5', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        accessibility: {
            point: {
                valueSuffix: '%'
            }
        },
        title: {
            text: '',
            style: {
                display: 'none'
            }
        },
        subtitle: {
            text: '',
            style: {
                display: 'none'
            }
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                borderWidth: 1,
                borderColor: '#FFF',
                dataLabels: {
                    enabled: false,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                }
            }
        },
        series: [{
            name: 'Utilisateurs',
            colorByPoint: true,
            showInLegend: true,
            data: [{
                name: 'Abonnés',
                y: data0,
                sliced: true,
                selected: true,
                color:'#2493ee86'
            },	{
                name: 'Désabonnés',
                y: data1,
                color:'#ee248286'
            }]
        }]
    });

    Highcharts.chart('container_6', {
        chart: {
            type: 'line'
        },
        title: {
            text: '',
            style: {
                display: 'none'
            }
        },
        xAxis: {
            categories: date_valuate
        },
        yAxis: {
            title: {
                text: 'Scores'
            }
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: false
                },
                enableMouseTracking: true
            }
        },
        series: [{
            name: 'AUC Score',
            data: hist_AUC
        }, {
            name: 'F1 Score',
            data: hist_F1
        }, {
            name: 'Recall Score',
            data: hist_Recall
        }, {
            name: 'Precision Score',
            data: hist_Precision
        }, {
            name: 'MCC Score',
            data: hist_MCC
        }, {
            name: 'Log Loss',
            data: hist_loss
        }],
    });