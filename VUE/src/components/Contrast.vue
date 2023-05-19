<template>
    <div>
        <div ref="chart" style="height: 500px;"></div>
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
                const response = await axios.get('http://127.0.0.1:5000/contrast');
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
                  title: {
                    text: 'Stacked Line'
                  },
                  tooltip: {
                    trigger: 'axis'
                  },
                  legend: {
                    data: ['Events', 'Tweets']
                  },
                  grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                  },
                  toolbox: {
                    feature: {
                      saveAsImage: {}
                    }
                  },
                  xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
                  },
                  yAxis: {
                    type: 'value'
                  },
                  series: [
                    {
                      name: 'Events',
                      type: 'line',
                      stack: 'Total',
                      data: this.chartData[0]
                    },
                    {
                      name: 'Tweets',
                      type: 'line',
                      stack: 'Total',
                      data: this.chartData[1]
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
