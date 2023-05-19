<template>
    <div>
        <div ref="chart" style="height: 600px;"></div>
        <h1>This is 2nd View</h1>
        <button @click="getData1">Update</button>
        <ul>{{string}}</ul>
    </div>
</template>

<script>
import axios from 'axios';
import * as echarts from 'echarts';

export default {
    name: 'FirstView',
    props: {
        msg: String
    },
    data() {
        return {
            string: 'nothing',
            chart: null,
            chartData: []
        };
    },
    methods: {
        async getData1() {
            try {
                const response = await axios.get('http://127.0.0.1:5000/life');
                console.log(response.data);
                this.chartData = response.data;
                this.updateChart();
            } catch (error) {
                console.log(error);
            }
        },
        updateChart() {
            this.chart.setOption(
                {
                  tooltip: {
                    trigger: 'item'
                  },
                  legend: {
                    top: '5%',
                    left: 'center'
                  },
                  series: [
                    {
                      name: 'Access From',
                      type: 'pie',
                      radius: ['40%', '70%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: 25,
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      data: this.chartData
                    }
                  ]
                }
            );
        },
    },
    mounted() {
        this.chart = echarts.init(this.$refs.chart);
        this.getData1();
    },
}
</script>
